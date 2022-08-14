from .models import CalorieTracker
from django.forms import ModelForm, TextInput


class CaloriesTrackerform(ModelForm):
    class Meta:
        model = CalorieTracker
        fields = ["username", "calories"]
        widgets = {
            'calories': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Amount of calories'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
        }
