from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
  
  """Time Stamped Model"""
  
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  
  class Meta:
    #추상화 -> 데이터 베이스에 등록 되지 않는다. 
    abstract = True