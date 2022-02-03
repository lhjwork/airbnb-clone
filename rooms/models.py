from importlib.metadata import packages_distributions
import os
from pyexpat import model 
from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
# Create your models here.


class AbstractItem(core_models.TimeStampedModel):
  
  """Abstract Item"""
  
  name = models.CharField(max_length=80)

  class Meta:
      abstract = True
    
  def __str__(self):
      return self.name
    
    
class RoomType(AbstractItem):
  
    pass

class Room(core_models.TimeStampedModel):
  
  
  """ Room Model Definition """
  
  name = models.CharField(max_length=140)
  description = models.TextField()
  country = CountryField()
  city = models.CharField(max_length=100)
  price = models.IntegerField()
  address = models.CharField(max_length=140)
  beds = models.IntegerField()
  bedsrooms = models.IntegerField()
  baths = models.IntegerField()
  check_in = models.TimeField()
  check_out = models.TimeField()
  instant_book = models.BooleanField(default=False)
  host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
  room_type = models.ManyToManyField(RoomType, blank=True)
  
   
def __str__(self):
    return self.name

  # __str__ method : 파이썬이 class를 발견하면 class를 마치 string 처럼 보여준다. ,모든 파이썬 class는 __str__ 을 
  # 가지고 있다.
#def __str__
