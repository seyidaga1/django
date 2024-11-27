from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/', blank=True, null=True)

    def __str__(self):
        return self.title
