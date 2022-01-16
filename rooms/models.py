from importlib.metadata import packages_distributions
import os 
from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
# Create your models here.

class Room(core_models.TimeStampedModel):
  
  name = models.CharField(max_length=140)
  description = models.TextField()
  country = CountryField()
  city = models.CharField(max_length=100)
  