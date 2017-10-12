from django.contrib import admin

# Register your models here.
from .models import (
    Person,
    Car, Manufacturer,
    Student,
    Fruit,
    Topping, Pizza,
    FacebookUser,InstagramUser,
    Membership, Group, Idol,
    Place, Restaurant,
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
admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Place)
admin.site.register(Restaurant)
