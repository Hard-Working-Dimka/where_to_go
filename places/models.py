from django.db import models


class Image(models.Model):
    place = models.ForeignKey('Place', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
    ordinal_number = models.IntegerField()

    def __str__(self):
        return f'{self.place} - {self.ordinal_number}'


class Place(models.Model):
    title = models.CharField(max_length=50)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title
