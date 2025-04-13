from django.db import models
from tinymce.models import HTMLField


class Image(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
    ordinal_number = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True)

    class Meta:
        ordering = ["ordinal_number"]
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.place} - {self.ordinal_number}'


class Place(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField(blank=True)
    long_description = HTMLField(blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    class Meta:
        unique_together = ['title', 'lng', 'lat']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title
