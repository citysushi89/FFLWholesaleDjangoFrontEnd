from django.db import models

# Create your models here.

class Data(models.Model):
    brand = models.TextField()
    model = models.TextField()
    price = models.TextField()
    quantity = models.TextField()
    link = models.TextField()
    vendor = models.TextField()

    def __str__(self):
        return self.item