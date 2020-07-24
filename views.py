from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User,auth
# Create your views here.
def signup(request):
    if request.method=="POST":
        first_name=request.POST['First Name']
        last_name=request.POST['Last Name']
        user_name=request.POST['user Name']
        password1=request.POST['Password1']
        password2=request.POST['Password2']
        email=request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif  User.objects.filter(email=email).exists():
                messages.info(request,'email is taken...if you already have an account click on login')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=user_name,password=password1,email=email)
                user.save()
                
                subject = 'Welcome to Haggle'
                message = 'Thank you '+first_name+' '+last_name+' for registering at Haggle.\n\nWith Regards\n'+'Haggle Team'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail( subject, message, email_from,[email,])

                print("user created successfully")
                return redirect('login')
                
        else:
            messages.info(request,'Password is not matching')
            '''return redirect('signup')'''
    else:
        return render(request,'signup.html')
def login(request):
     if request.method=="POST":
        user_name=request.POST['user Name']
        password=request.POST['Password']

        user=auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials..')
            return redirect('login')
     else:
         return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

