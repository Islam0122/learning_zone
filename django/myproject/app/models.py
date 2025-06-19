from django.db import models

class Car(models.Model):
    image = models.ImageField(upload_to='car_images')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.CharField(max_length=100)
    description = models.TextField()
    year_built = models.DateField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
