import time

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image
import requests
import sys

SLEEP_TIME = 90


def add_json_to_db(url):
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    place, _ = Place.objects.get_or_create(
        title=response['title'],
        short_description=response['description_short'],
        long_description=response['description_long'],
        defaults={'lng': response['coordinates']['lng'], 'lat': response['coordinates']['lat']}
    )

    for number_of_image, image in enumerate(response['imgs'], start=0):
        try:
            image_response = requests.get(image)
            image_response.raise_for_status()
        except requests.exceptions.HTTPError:
            sys.stderr.write(f'Произошла ошибка при загрузке фотографии : {image}\n')
            continue
        except requests.exceptions.ConnectionError:
            sys.stderr.write('Произошла ошибка с подключением к сети!\n')
            time.sleep(SLEEP_TIME)
            continue

        place.images.create(
            image=ContentFile(image_response.content, f'{place.title}_{number_of_image}.jpg'),
            ordinal_number=number_of_image
        )


class Command(BaseCommand):
    help = 'Add demo data to database'

    def handle(self, *args, **options):
        if options['url']:
            add_json_to_db(options['url'])

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            nargs='?',
            help='URL на JSON файл с данными',
        )
