from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

class CalorieTracker(models.Model):
    user = models.CharField('Enter username', max_length=50)
    calories = models.PositiveIntegerField('Amount of calories')
    datetime = models.DateField(auto_now_add=False, auto_now=False, blank=True, null = True)
    def __str__(self):
        return self.user
