from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['place_image', ]

    def place_image(self, obj):
        height = obj.image.height
        width = obj.image.width
        if height > 200:
            height = 200
        if width > 200:
            width = 200 #TODO: посмотреть с лямбдой

        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=width,

            height=height
        )
        )


@admin.register(Place)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', ]
    search_fields = ['title', ]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'ordinal_number',]
    list_editable = ['ordinal_number', ]
    search_fields = ['place', ]
