from django.shortcuts import render,redirect
from .models import *

# Create your views here.

# view for register page 

def RegisterPage(request):
    return render(request,"registrationapp/register.html")

# views for user registration

def UserRegistration(request):
    if request.method=="POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        # First we will validate that user already exist
        user = User.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request,"registrationapp/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(FirstName=fname,LastName=lname,Email=email,Contact=contact,Password=password)
                message = "User register successfully"
                return render(request,"registrationapp/login.html",{'msg':message})
            else:
                message = "Confirm password doesnot match"
                return render(request,"registrationapp/register.html",{'msg':message})
            

# login page view

def LoginPage(request):
    return render(request,"registrationapp/login.html")

# login user

def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # checking the emailid with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password == password:
                # we are getting user data in session 
                request.session['FirstName'] = user.FirstName
                request.session['LastName'] = user.LastName
                request.session['Email'] = user.Email
                
                return render(request,"registrationapp/home.html")
            else:
                message = "Password does not matched"
                return render(request,"registrationapp/login.html",{'msg':message})
        else:
            message = "User doen not exist"
            return render(request,"registrationapp/register.html",{'msg':message})
        


# home page view

def HomePage(request):
    return render(request,"registrationapp/home.html")

# upload image view

def UploadImage(request):
    if request.method=="POST":
        imagename = request.POST['imgname']
        pics = request.FILES['image']

        newimg = ImageData.objects.create(imagename=imagename,Image=pics)
        return redirect('showimg')    
# Image fetching view

def ImageFetch(request):
    all_img = ImageData.objects.all()
    return render(request,"registrationapp/show.html",{'key3':all_img})