
from dataclasses import field
from typing_extensions import Required
from  rest_framework  import serializers

from accounts import email
from . models import *
from django.contrib.auth.hashers import make_password


class registeruser_serializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['username','email','password','first_name','last_name']


class Login_serilizer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class verifyotp_serializer(serializers.Serializer):
    email = serializers.CharField()
    otp = serializers.IntegerField()
    
    
class student_serializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'
   




    # def create(self, validated_data):
    #     user = myUser.objects.create(
    #         username = validated_data['username'],
    #         email = validated_data['email'],
    #         password = make_password(validated_data['password']),  
       
    #     )
    #     user.save()  
    #     return user
        


    