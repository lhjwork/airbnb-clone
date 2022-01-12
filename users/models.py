from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 모델은 데이터가 보여지는 모습에 해당한다.
class User(AbstractUser): 
  
    bio = models.TextField(default="")