from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.RegisterPage,name="registerpage"),
   path("register/",views.UserRegistration,name="register"),
   path("loginpage/",views.LoginPage,name="loginpage"),
   path("loginuser/",views.LoginUser,name="login"),
   path("homepage/",views.HomePage,name="homepage"),
   path("imageupload/",views.UploadImage,name="imageupload"),
   path("showimg/",views.ImageFetch,name="showimg"),
]