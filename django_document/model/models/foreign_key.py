from django.db import models

__all__ = (
    'Manufacturer',
    'Car',
    'Student',
)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return (f'{self.manufacturer} - {self.name}')


class Student(models.Model):
    """
    Recurisve Relationship Example
    """
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    def save(self, *args, **kwargs):
        if self.teacher == self:
            print('teacher cannot be self')
            self.teacher = None
        super().save(*args, **kwargs)

    def __str__(self):
        return (self.name)
