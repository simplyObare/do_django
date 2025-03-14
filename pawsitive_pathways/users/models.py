from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True, error_messages={"unique": "A user with this email already exists."}
    )
    username = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def clean(self):
        super().clean()

        if self.username and len(self.username) < 3:
            raise ValidationError(
                {"username": "Username must have at least 3 characters."}
            )


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=50, blank=True, null=True)
    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0, "Age cannot be negative."),
            MaxValueValidator(50, "Age cannot exceed 50."),
        ],
    )
    special_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.species})"
