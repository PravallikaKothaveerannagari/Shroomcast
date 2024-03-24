import datetime

from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class VisualCrossingAuth(models.Model):
    vc_key = models.CharField(max_length=25)

class Query(models.Model):
    query_count = models.IntegerField(default=0)
    day = models.DateField(default=datetime.date.today)