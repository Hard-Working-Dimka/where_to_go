from django.db import models
from tinymce.models import HTMLField


class Image(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images', verbose_name='место')
    image = models.ImageField(verbose_name='фотография')
    ordinal_number = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True,
                                                 verbose_name='порядковый номер')

    class Meta:
        ordering = ['ordinal_number']
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f'{self.place} - {self.ordinal_number}'


class Place(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    short_description = models.TextField(blank=True, verbose_name='краткое описание')
    long_description = HTMLField(blank=True, verbose_name='полное описание')
    lng = models.FloatField(verbose_name='долгота')
    lat = models.FloatField(verbose_name='широта')

    class Meta:
        unique_together = ['title', 'lng', 'lat']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title
