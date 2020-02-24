from django.db import models
import datetime
# Create your models here.
class CalculationLog(models.Model):
    X = models.FloatField()
    Y = models.FloatField()
    Result = models.FloatField()
    timestamp = models.DateTimeField('cal_time', null=True, default=datetime.datetime.now)