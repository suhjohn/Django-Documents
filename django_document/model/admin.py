from django.contrib import admin

# Register your models here.
from .models import Person, Manufacturer, Student, Car, Fruit

admin.site.register(Person)
admin.site.register(Manufacturer)
admin.site.register(Student)
admin.site.register(Car)
admin.site.register(Fruit)
