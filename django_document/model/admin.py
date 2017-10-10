from django.contrib import admin

# Register your models here.
from .models import (
    Person,
    Manufacturer,
    Student,
    Car,
    Fruit,
    Topping,
    Pizza,
    FacebookUser,
    InstagramUser
)

admin.site.register(Person)
admin.site.register(Manufacturer)
admin.site.register(Student)
admin.site.register(Car)
admin.site.register(Fruit)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)