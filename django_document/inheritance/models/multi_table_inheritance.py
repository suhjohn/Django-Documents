from django.db import models

__all__ = (
    'Place',
    'Restaurant',
)

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} Restaurant'


"""
place 에서 supplier를 호출
place customers_set
"""
