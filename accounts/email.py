

from email import message
from django.core.mail import send_mail
import random
from . models import *

from django.conf  import settings

def send_otp_email(email):
    subject = 'Your account Varification mail'
    otp = random.randint(1000,20000)
    message = f'your Otp is {otp}'  
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])

    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()










# def mysend_mail():
#     otp = random.randint(1000,20000)
#     email_send = send_mail(
#         'New Tech Python ',
#         f'Register Sucessfully  ,{otp}   is your OTP',
#         'sajal89304@gmail.com',
#         ['sajal2217211@gmail.com'],
#         fail_silently=False,
#     )



#     return email_send
    





















'''    class registeruser(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = registeruser_serializer(data=data)

            if serializer.is_valid():
                serializer.save()
                send_otp_email(serializer.data['email'])
                return Response(
    '''