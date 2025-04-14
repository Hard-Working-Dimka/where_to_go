from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image
from adminsortable2.admin import SortableStackedInline, SortableAdminBase

IMAGE_MAX_WIDTH = 200
IMAGE_MAX_HEIGHT = 200


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['place_image', ]
    extra = 10

    def place_image(self, obj):
        return format_html('<img src="{url}" style="max-width:{max_width}px; max-height:{max_height}px" />',
                           url=obj.image.url,
                           max_width=IMAGE_MAX_WIDTH,
                           max_height=IMAGE_MAX_HEIGHT, )


@admin.register(Place)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'id', ]
    search_fields = ['title', ]
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'ordinal_number', ]
    list_editable = ['ordinal_number', ]
    search_fields = ['place', ]
    autocomplete_fields = ['place', ]
