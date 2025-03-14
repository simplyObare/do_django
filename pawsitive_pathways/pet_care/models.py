from django.db import models
from users.models import Pet, User


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.CASCADE, related_name="services"
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="service_images/", blank=True, null=True)

    def __str__(self):
        return self.name


class PetServiceSelection(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pet_service_selections"
    )
    pet = models.ForeignKey(
        Pet, on_delete=models.CASCADE, related_name="pet_service_selections"
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="service_selections"
    )
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.pet.name} - {self.service.name} on {self.date} at {self.time}"
