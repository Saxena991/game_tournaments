from django.contrib.auth import authenticate, login
#from django.http import HttpResponse
#from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from user.models import UserProfile
from django.contrib import auth
from tournament.models import Tournament
from datetime import datetime
import time
# Create your views here.
def mainpage(request):
    return render(request, 'main.html')

def home(request):
    tournament_detail = Tournament.objects.all()

    data = {'tournament_detail': tournament_detail}


    # title = "Home"  # Set the title here
    # context = {'title': title}
    return render(request, 'home.html',data)

def tournament(request):
    title = "Tournament"  # Set the title here
    context = {'title': title}

    return render(request, 'tournament.html',context)

def gallery(request):
    title = "gallery"  # Set the title here
    context = {'title': title}
    return render(request, 'gallery.html',context)

def contact(request):
    title = "contact"  # Set the title here
    context = {'title': title}
    return render(request, 'contact.html',context)

def success(request):
    return render(request, 'success.html')

########################## for signup ####################
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Create a new user instance
        my_user = UserProfile(username=username, email=email, password=password)
        my_user.save()

        return redirect('login_user')
    return render(request, 'signup.html')

######################## for login ##########################
def login_user(request):
    error_message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        try:
            user_profile = UserProfile.objects.get(username=username)
        except UserProfile.DoesNotExist:
            user_profile = None
        if user_profile and user_profile.password == password:
            return redirect('home')  
        else:
            error_message = ("Invalid Username or Password Please try Again!.")
    return render(request, 'login.html',{'error_message':error_message})


################## for logout ############################
def logout(request):
    auth.logout(request)
    return redirect('/')






























    # Use the 'authenticate' function to check the username and password
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         # If 'authenticate' returns a user, log them in
    #         login(request, user)
    #         return redirect('home')
    #     else:
    #         error_message = "Invalid Username or Password Please try Again!."
            

    #         #return redirect('login')
 
    # return render(request, 'login.html',{'error_message':error_message})








