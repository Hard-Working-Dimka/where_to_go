from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Place


def show_index(request):
    places = Place.objects.all()
    features = []

    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": reverse('place', args=[place.id])
            }
        }

        features.append(feature)

    context = {
        "type": "FeatureCollection",
        "features": features,
    }
    data = {"context": context}

    return render(request, 'index.html', context=data)


def show_place(request, id):
    place = get_object_or_404(Place, pk=id)
    images = place.images.all()

    urls = []
    for image in images:
        urls.append(image.image.url)
    place_dict = model_to_dict(place, fields=["title", "description_short", "description_long"])

    place_dict["coordinates"] = [place.lng, place.lat]
    place_dict["imgs"] = urls

    return JsonResponse(place_dict, safe=False, json_dumps_params={'ensure_ascii': False})
