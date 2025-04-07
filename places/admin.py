from django.contrib import admin
from .models import Place, Image

@admin.register(Place)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', ]
    search_fields = ['title', ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [ 'place', 'ordinal_number']
    list_editable = ['ordinal_number', ]

