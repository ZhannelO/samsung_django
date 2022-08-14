from .models import CalorieTracker
from django.forms import ModelForm, TextInput, DateInput


class CaloriesTrackerform(ModelForm):
    class Meta:
        model = CalorieTracker
        fields = ['user', "calories", 'datetime']
        widgets = {
            'calories': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Amount of calories'
            }),
            "user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            "datetime": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date (year-month-day) ',
            }, format='%Y-%m-%d')
        }
