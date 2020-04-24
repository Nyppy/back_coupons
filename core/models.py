from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.name)


class CouponsOjects(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    photo = models.ImageField()
    name = models.CharField(max_length=30)
    price_service = models.CharField(max_length=30)
    price_sail = models.CharField(max_length=30)
    end_data = models.DateField()
    summary = models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)