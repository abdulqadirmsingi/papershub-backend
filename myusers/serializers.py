from rest_framework import serializers
from .models import User
from djoser.serializers import UserCreateSerializer, UserSerializer, TokenCreateSerializer, TokenSerializer



   
   
   

class UserCreaterSerializer(UserCreateSerializer):
   class Meta(UserCreateSerializer.Meta):  
       fields = ['id','first_name', 'last_name', 'phone_number','email','password','year','degree_program']#

class CurrentUserSerializer(UserSerializer):
   class Meta(UserSerializer.Meta):
      fields = ['email', 'id','first_name', 'last_name', 'year', 'degree_program']  
      