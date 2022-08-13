
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CalorieTracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calories = models.PositiveIntegerField('Amount of calories')

    def __str__(self):
        return str(self.user)