from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image
import requests


def add_json_to_db(url):
    response = requests.get(url)
    response.raise_for_status()
    response = response.json()
    place = Place.objects.get_or_create(
        title=response['title'],
        description_short=response['description_short'],
        description_long=response['description_long'],
        lng=response['coordinates']['lng'],
        lat=response['coordinates']['lat'],
    )[0]

    ordinal_number = 0
    for number_of_image, image in enumerate(response['imgs'], start=0):
        image_response = requests.get(image)
        image_response.raise_for_status()

        place.images.create(
            image=ContentFile(image_response.content, f'{place.title}_{number_of_image}.jpg'),
            ordinal_number=ordinal_number
        )
        ordinal_number += 1


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

# https://raw.githubusercontent.com/devmanorg/where-to-go-places/refs/heads/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json
