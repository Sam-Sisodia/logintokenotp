
from re import T
from urllib import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from . serializer import *
# Create your views here.

from django.core.mail import send_mail
import random
from rest_framework.generics import CreateAPIView
from  rest_framework.views import APIView
from . email import *

from  rest_framework.viewsets import ModelViewSet

from . models import *


class registeruser(APIView):
    def post(self,request):
        try:
            serializer = registeruser_serializer(data=request.data)
              
            if serializer.is_valid():
                user = User.objects.create(
                username =  serializer.validated_data['email'],
                first_name =  serializer.validated_data['first_name'],
                last_name =  serializer.validated_data['last_name'],
                email =  serializer.validated_data['email'],
                password =  serializer.validated_data['password'])
                print(user)
                

                user.set_password(user.password)
                user.is_active=False
                user.save()
                send_otp_email(serializer.data['email'])
                #send_otp_email(serializer.data['email'])
                return Response(
                    {
                        'status':200,
                        'message':'Register Sucessfully',
                        'data' :serializer.data
                    }
                )
            return Response({
                'status':400,
                'msg':'something went wrong',
                'data' :serializer.errors
            })

        except Exception as e :
            print(e)
            return Response({
                 'msg':'Try Again '

            })



class VerifyOTP(APIView):
    def post(self,request):
        try:
            serializer = verifyotp_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                email = serializer.validated_data['email']
               # password = serializer.validated_data['password']
                otp = serializer.validated_data['otp']
                user = User.objects.get(email=email)
                if user:
                    if user.is_active is True:
                        return Response("Already Verified ")
                    elif user.otp == otp :
                        user.is_active = True
                        user.save()
                        return Response("Verified sucessfully")
                    else:
                        return Response("Invaild otp ")
                else:
                    return Response("User not exit")       
        except Exception as e:
            print(e)
            return Response({
                 'msg' : 'Somethig went wrong' })


from django.contrib.auth import authenticate , login , logout

from rest_framework.authtoken.models import Token


class Loginuser(APIView):
    
    def post(self,request,*args, **kwargs):
        serializer = Login_serilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password= serializer.validated_data['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request,user)
                user = User.objects.get(username= serializer.data['email'])
                token_obj , _ = Token.objects.get_or_create(user=user)
                return Response({ 'token' : str(token_obj),  'status':200  })

            if user is None:
                return Response( status=status.HTTP_400_BAD_REQUEST)

     
        
    


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class studentview(ModelViewSet):
    permission_classes  = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


    queryset = StudentDetails.objects.all()
    serializer_class = student_serializer


# {
#   "token": "775bafb6fde3c74e06d85e03d07d2ef9c28c8ba5"
# }


#   token = get_tokens_for_user(user)
               # return Response(token, status=status.HTTP_200_OK)