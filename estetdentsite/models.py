from django.db import models


class Spec(models.Model):
    name = models.CharField(max_length=256)
    spec = models.CharField(max_length=256)
    info = models.TextField()
    photo = models.ImageField(upload_to='spec_photo', blank=True)

    def __str__(self):
        return self.name

# Create your models here.
class Service (models.Model):
    name = models.CharField(max_length=256)
    info = models.TextField()
    price = models.IntegerField()