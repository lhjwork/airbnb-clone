from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 모델은 데이터가 보여지는 모습에 해당한다.
class User(AbstractUser): 
  
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN ="kr"
    
    LANGUAGE_CHOICES =((LANGUAGE_ENGLISH, "English"),(LANGUAGE_KOREAN,"Korean"))
    
    CURRENCY_USD = "usd"
    CURRENCY_KRD = "krw"
    
    Male = "male"
    Female = "Female" 
    GENDER_CHOICES=((Male,"ma"),(Female,"fe"))
    

    CURRENCY_CHOICES = ((CURRENCY_USD,"USD"),(CURRENCY_KRD,"KRW"))
    avatar = models.ImageField(default="",null=True, blank=True)
    gender = models.CharField(default="",choices=GENDER_CHOICES,max_length=10, null=True,blank= True)
    bio = models.TextField(default="",blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=10,null=True,blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES,max_length=10,null=True,blank=True)
    superhost = models.BooleanField(default=False)
    
    
    superhost =models.BooleanField(default=False,null=True)