from django.db import models

__all__ = (
    'Pizza',
    'Topping',
    'TwitterUser',
)


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    topping = models.ManyToManyField(
        'Topping',
        blank=True,
    )

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField(
        'self',
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.name