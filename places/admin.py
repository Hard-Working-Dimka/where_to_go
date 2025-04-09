from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['place_image', ]
    extra = 10

    def place_image(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=(lambda x: 200 if x > 200 else x)(obj.image.width),
            height=(lambda x: 200 if x > 200 else x)(obj.image.height)
        )
        )


@admin.register(Place)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ['title', 'id', ]
    search_fields = ['title', ]
    inlines = [
        ImageInline,
    ]


# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ['place', 'ordinal_number', ]
#     list_editable = ['ordinal_number', ]
#     search_fields = ['place', ]
