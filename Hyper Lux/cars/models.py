from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SuperCar(models.Model):

    # Basic details
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color = models.CharField(max_length=50)

    # Relationships
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="cars"
    )

    # Specifications
    engine = models.CharField(max_length=200)
    horsepower = models.PositiveIntegerField()
    top_speed = models.PositiveIntegerField(help_text="Speed in km/h")
    acceleration = models.DecimalField(
        max_digits=4, decimal_places=2, help_text="0-100 km/h in seconds"
    )
    fuel_type = models.CharField(
        max_length=50,
        choices=[
            ("Petrol", "Petrol"),
            ("Diesel", "Diesel"),
            ("Hybrid", "Hybrid"),
            ("Electric", "Electric"),
        ],
    )

    # Media
    exterior_image1 = models.ImageField(upload_to="supercars/exteriors/", blank=False)
    exterior_image2 = models.ImageField(upload_to="supercars/exteriors/", blank=False)
    exterior_image3 = models.ImageField(upload_to="supercars/exteriors/", blank=False)
    exterior_image4 = models.ImageField(upload_to="supercars/exteriors/", blank=False)
    interior_image = models.ImageField(upload_to="supercars/interiors/", blank=False)

    # Miscellaneous
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.color} {self.make} {self.model} ({self.year})"
