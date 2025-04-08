from django.shortcuts import render
from .models import Place


def show_index(request):
    #     detailsurl = {
    #     "title": "Экскурсионный проект «Крыши24.рф»",
    #     "imgs": [
    #         "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/af7b8599fec9d2542a011f1d01d459e2.jpg",
    #         "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/965c5a3ff5b2431e646d30b6744afd2d.jpg",
    #         "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/06868b2b01ff8db506cd21956a6cb636.jpg",
    #         "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a8cc3e03f56413275ded99e51226a70f.jpg",
    #         "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/44e96733303e7490aaa1cf2eebfbbfff.jpg",
    #         "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/fadf618505b087fa539e883f33f850b2.jpg",
    #         "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/ec461a89a1d0d5a4cb7c81f1fc0a4e89.jpg"
    #     ],
    #     "description_short": "Хотите увидеть Москву с высоты и разделить яркие впечатления с друзьями? В этом поможет проект «Крыши24.рф». Вы можете выбрать крышу из множества интересных вариантов и провести там свидание, вечеринку, творческое занятие, фотосессию или что-то ещё.",
    #     "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии и мероприятия на крышах, откуда открываются впечатляющие виды на мегаполис. </p><h4>Экскурсии на высоте</h4><p>Список крыш, на которые можно подняться, очень велик, и находятся они в разных уголках города. Оттуда видны достопримечательности и красивейшие городские панорамы, так что это отличная возможность заново открыть для себя Москву. Экскурсии безопасны, на эти крыши можно подниматься с детьми. Перед подъёмом опытный гид проведёт инструктаж и будет сопровождать вас во время прогулки.</p><p>С крыш, доступных для посещения, вы увидите «Москва Сити» вблизи, стадион «Лужники», Новодевичий монастырь, Красную и Киевскую площади, мост Богдана Хмельницкого, сталинские высотки, Новый Арбат, и многие другие знаковые места столицы. </p><p>Стоимость экскурсии — 1250 рублей, продолжительность — 1 час. В стоимость экскурсии включены услуги гида.</p><h4>Свидания на высоте птичьего полёта</h4><p>А ещё «Крыши24.рф» — настоящая находка для тех, кто хочет устроить незабываемое романтическое свидание. Выбирайте свой вариант из пяти крыш, расположенных рядом с главными достопримечательностями, и удивите любимого человека. </p><p>На крыше для вас устроят зону отдыха с пледами и подушками. В стоимость также входят свечи, цветок, бокалы, столовые приборы, фруктовая тарелка и напиток. А если ваше событие более строгое и торжественное, то для вас поставят праздничный стол и стулья. За дополнительную плату вы можете заказать букет цветов, воздушные шары, музыканта, виниловый проигрыватель, салют, напитки и еду. </p><p>Базовая стоимость свидания — 5500 рублей, продолжительность — 2 часа.</p><p><strong>Фотосессии над Москвой</strong></p><p>Необычным подарком для себя и для любимых может стать фотосессия на крышах. Из полусотни вариантов крыш вам помогут выбрать ту, которая подойдёт именно вам. На сессии будет работать профессиональный руфер-фотограф с опытом более 10 лет. В итоге вы получите около 100 фотоснимков, 15 из них — уже обработанными, так что их можно будет сразу выкладывать в соцсети и удивлять друзей.</p><p>Стоимость фотосессии — от 4000 рублей, продолжительность — 1 час. </p><p>Также проект «Крыши24.рф» организует девичники, вечеринки, творческие мероприятия и многое другое.</p><p>Узнать подробности можно на <a class=\"external-link\" href=\"https://www.крыши24.рф/\" target=\"_blank\">официальном сайте</a> и в <a class=\"external-link\" href=\"https://instagram.com/roof24_moscow/\" target=\"_blank\">Instagram</a>.</p>",
    #     "coordinates": {
    #         "lng": "37.32478399999957",
    #         "lat": "55.70731600000015"
    #     }
    # }
    places = Place.objects.all()
    features = []

    for place in places:
        index = + 1
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": index,
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/refs/heads/master/places/moscow_legends.json"
            }
        }

        features.append(feature)

    context = {
        "type": "FeatureCollection",
        "features": features,
    }
    data = {"context": context}

    return render(request, 'index.html', context=data)
