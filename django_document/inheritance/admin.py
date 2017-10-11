from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, School, Place, Restaurant

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Restaurant)
