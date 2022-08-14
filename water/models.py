from django.db import models
from django.contrib.auth.models import User

class CalorieTracker(models.Model):
    username = models.CharField('Enter username', max_length=50)
    calories = models.PositiveIntegerField('Amount of calories')

    def __str__(self):
        return self.username
