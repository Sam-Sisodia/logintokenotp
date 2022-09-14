
from dataclasses import field
import re
from typing_extensions import Required
from  rest_framework  import serializers

from accounts import email
from . models import *
from django.contrib.auth.hashers import make_password


class registeruser_serializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['email','password','first_name','last_name']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email already exists!.")
        return value
    def validate_first_name(self,value):
        if value == "":
            raise serializers.ValidationError("The firstname cannot be empty")
        return value

    def validate_last_name(self,value):
        if value == "":
            raise serializers.ValidationError("The lastname cannot be empty")
        return value
            


    


class Login_serilizer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


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
        


    