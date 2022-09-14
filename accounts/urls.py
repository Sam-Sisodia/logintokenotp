from django.contrib import admin
from django.urls import path,include
from  accounts import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student',views.studentview , basename="students")

urlpatterns = [
    path('',views.registeruser.as_view()),
    path('ve',views.VerifyOTP.as_view()),
    path('login', views.Loginuser.as_view()),

    path ('stu', include(router.urls)),

]