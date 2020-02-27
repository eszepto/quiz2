from django.db import models
import datetime


# Create your models here.
class CalculationGetLog(models.Model):
    X = models.FloatField()
    op = models.CharField(max_length=1)
    Y = models.FloatField()
    Result = models.FloatField()
