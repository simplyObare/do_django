from django import forms
from .models import PetServiceSelection


class PetServiceSelectionForm(forms.ModelForm):
    class Meta:
        model = PetServiceSelection
        fields = ["pet", "service", "date", "time"]
        widgets = {
            "pet": forms.Select(
                attrs={
                    "class": "form-select w-full rounded-lg border-gray-300 focus:ring-blue-500",
                }
            ),
            "service": forms.Select(
                attrs={
                    "class": "form-select w-full rounded-lg border-gray-300 focus:ring-blue-500",
                }
            ),
            "date": forms.DateInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "type": "date",
                }
            ),
            "time": forms.TimeInput(
                attrs={
                    "class": "form-input w-full rounded-lg border-gray-300 focus:ring-blue-500",
                    "type": "time",
                }
            ),
        }
