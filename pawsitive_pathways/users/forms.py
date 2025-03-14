from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Pet


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Enter your username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Enter your email",
                }
            ),
            "password1": forms.PasswordInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Enter your password",
                }
            ),
            "password2": forms.PasswordInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Confirm your password",
                }
            ),
        }

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username and len(username) < 3:
            raise forms.ValidationError("Username must have at least 3 characters.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                "placeholder": "Enter your email",
            }
        ),
        label="Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                "placeholder": "Enter your password",
            }
        ),
        label="Password",
    )


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "species", "breed", "age", "special_notes"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Pet's name",
                }
            ),
            "species": forms.TextInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Species (e.g., dog, cat)",
                }
            ),
            "breed": forms.TextInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Breed (optional)",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Age in years",
                }
            ),
            "special_notes": forms.Textarea(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "placeholder": "Special notes (optional)",
                    "rows": 4,
                }
            ),
        }
