from django.contrib import admin
from .models import Category, Feature, SuperCar, CarImage

# Register your models here.
admin.site.register(Category)
admin.site.register(Feature)
admin.site.register(SuperCar)
admin.site.register(CarImage)
