from django.db import models
import datetime


# Create your models here.
class CalculationGetLog(models.Model):
    X = models.FloatField()
    Y = models.FloatField()
    Result = models.FloatField()
