from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.urls import reverse


def home_screen_view(request):
    print(request.headers)
    return render(request,"personal/home.html",{})
def homelogin(request):
    return render(request,"personal/login.html")
def signup(request):
    if request.method=="POST":
        username=request.POST.get("username",None)
        first_name=request.POST.get("firstname",None)
        last_name=request.POST.get("lastname",None)
        email=request.POST.get("email",None)
        password=request.POST.get("password",None)

        user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)


        return redirect('signin')
    return render(request,"personal/signup.html")
def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username, password=password)

        if user is not None:
            login(request,user)

            return redirect(reverse('profile', args=()))
        else:
            return redirect(reverse('home_login',args=()))
    return render(request,"personal/signin.html")
def signout(request):
    logout(request)
    return redirect(reverse("signin"))
def profile(request):
    if request.user.is_authenticated:
        return  render(request,"personal/profile.html")
    else:
        return redirect(reverse('signin'))
def sleeptracker(request):
    if request=="POST":
        falling_asleep=request.POST.get("f_asleep_time")
        waking_up=request.POST.get("getting_up")
        messages.info(request,f"you will sleep {falling_asleep*60+waking_up} minutes")
    return render(request, 'personal/sleeptracker.html')


def caloriestracker(request):
    if request.method == "POST":
        amount_of_calories = request.POST.get("amount of calories")
        messages.info(request,f"{amount_of_calories} calories is not enough for you, darling")
    return render(request, 'personal/caloriestracker.html')

