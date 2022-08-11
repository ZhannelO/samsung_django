from .models import CalorieTracker
from django.forms import ModelForm, TextInput


class CaloriesTrackerform(ModelForm):
    class Meta:
        model = CalorieTracker
        fields = ["calories"]
        widgets = {
            'calories': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Amount of calories'
            })
        }