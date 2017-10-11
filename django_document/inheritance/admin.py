from django.contrib import admin

# Register your models here.
from inheritance import Student, Teacher

admin.site.register(Student)
admin.site.register(Teacher)
