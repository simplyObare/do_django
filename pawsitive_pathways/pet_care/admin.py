from django.contrib import admin
from django.utils.html import format_html
from .models import ServiceCategory, Service, PetServiceSelection


# Register the ServiceCategory model
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


# Register the Service model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
    )
    list_filter = ("category",)
    search_fields = ("name", "category__name")


# Register the PetServiceSelection model
@admin.register(PetServiceSelection)
class PetServiceSelectionAdmin(admin.ModelAdmin):
    list_display = ("user", "pet", "service", "date", "time")
    list_filter = ("service", "date", "time")
    search_fields = (
        "user__email",
        "pet__name",
        "service__name",
    )
