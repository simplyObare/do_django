from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100, unique=True)
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
    features = models.ManyToManyField(Feature, related_name="cars")

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

    # Miscellaneous
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.make}-{self.model}-{self.year}")
            slug = base_slug
            counter = 1

            while SuperCar.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.color} {self.make} {self.model} ({self.year})"


class CarImage(models.Model):
    class ImageCategory(models.TextChoices):
        SIDE_VIEW = "Side View", "Side View"
        DOORS_OPEN = "Doors Open", "Doors Open"
        ENGINE = "Engine", "Engine"
        INTERIOR = "Interior", "Interior"
        FROM_BEHIND = "From Behind", "From Behind"

    car = models.ForeignKey("SuperCar", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="supercars/")
    category = models.CharField(
        max_length=50, choices=ImageCategory.choices, default=ImageCategory.SIDE_VIEW
    )
    is_exterior = models.BooleanField(default=True)
    alt_text = models.CharField(
        max_length=255, default="Image of an amazing supercar", editable=False
    )

    def save(self, *args, **kwargs):
        if self.car:
            self.alt_text = (
                f"{self.car.year} {self.car.make} {self.car.model} - {self.category}"
            )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category} image of {self.car if self.car else 'Unknown Car'}"
