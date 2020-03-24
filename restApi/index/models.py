from django.db import models

# Create your models here.
class FixedGoal(models.Model):
    image = models.CharField(max_length=100)
    tittle = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

