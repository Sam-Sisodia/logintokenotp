# from http import server
# import smtplib

# server = smtplib.SMTP_SSL("smtp.gmail.com",465)
# server.login("sajal89304@gmail.com","Pfqpvlgygsmjxabc")
# server.sendmail("sajal89304@gmail.com" ,"mohan.pandit@visiontrek.in" , "hello sir this is my  ")
# print("message send ")
# server.quit()

















# import smtplib, ssl

# port = 587  # For SSL
# password = 'Pfqpvlgygsmjxabc'

# # Create a secure SSL context
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("sajal89304@gmail.com", password)
#     # TODO: Send email here







# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MzIyMDk5OSwiaWF0IjoxNjYzMTM0NTk5LCJqdGkiOiI3NDBjNDI0YjU2Zjk0NDk5YTAwMDY4YTg3ODI5ODhkYiIsInVzZXJfaWQiOjE4fQ.F9BeUUUs8qFDlYuh3353ynjlTOCecCkSeEY10GbbaXM",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzMTM0ODk5LCJpYXQiOjE2NjMxMzQ1OTksImp0aSI6IjkxYTY0MWMwYjRkZTQ0MjdiNDVmNGQ1M2I2MGQ1ZWFhIiwidXNlcl9pZCI6MTh9.H7dCfF3-a6dcJ8wdnWB5TXukNXP7-oATbQl3-Og0UPI"
# }




# class VerifyOTP_my(CreateAPIView):
#     queryset = ""
#     serializer_class = verifyotp_serializer
#     def create(self,request):
#         try:
#             serializer = verifyotp_serializer(data=request.data)
#             if serializer.is_valid(raise_exception=True):
#                 otp = serializer.validated_data['otp']
#                 serializer.save()
      
#                 user = User.objects.get(email=email)
                
                
#                 if user.otp == otp:
#                     print(user.otp)
#                     #user.password = password
#                     user.is_verified = True
#                     user.is_active = True
#                     user.save()
#                     return Response("Nice Work ")
#                 else:
#                     return Response("Bad Work  ")


                
          
           
#         except Exception as e:
#             print(e)
#             return Response({
#                  'msg' : 'Somethig went wrong' })














'''
{    "username":"stinas",
    "first_name" :"JJ",
    "last_name" :"00",
     "email" :"sat@yopmail.com",
    "password": "1234"
}'''




















'''def mysend_mail(request):
    otp = random.randint(1000,20000)

    send_mail(
        'python  testing mail',
        f'Pthon  message here -  {otp}   is your OTP',
        'sajal89304@gmail.com',
        ['thephoenixxperson@gmail.com'],
        fail_silently=False,
    )
    return render(request , "hi.html")'''











'''    class registeruser(APIView):
    def post(self,request):
        try:
            data = request.data
            serializer = registeruser_serializer(data=data)

            if serializer.is_valid():
                serializer.save()
                send_otp_email(serializer.data['email'])
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
            return Response({
                 'msg':'Try Again '
            })
'''



























# import smtplib,ssl

# server = smtplib.SMTP('smtp.gamil.com',587)
# server.starttls()

# server.login('sajal89304@gmail.com','pfqpvlgygsmjxabc')

# server.sendmail('sajal89304@gmail.com', 'sajalkumar801@gmail.com','Hello this is my first mail from python')


# print("Mail Sent Successfully ")









# sender_email = "sajal89304@gmail.com"
# password = "sajal801"
 
# recevier_email = ['sajalkumar801@gmail.com']

# email_string = f "subject : Mail from Sajal To : {','.join } 