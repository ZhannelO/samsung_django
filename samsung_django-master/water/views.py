from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
from django.urls import reverse
from .forms import CaloriesTrackerform

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
    if request.method=="POST":
        falling_asleep=request.POST["f_asleep_time"].split(":")
        waking_up=request.POST["getting_up"].split(":")

        h=[]
        for i in falling_asleep:
            t=[]
            for j in i:
                t.append(j)
            if t[0]=="0":
                h.append(t[1])
            else:
                h.append("".join(t))
        h2=[]
        for i in waking_up:
            n=[]
            for j in i:
                n.append(j)
            if t[0]=="0":
                h2.append(t[1])
            else:
                h2.append("".join(n))
        minutes_wup=int(waking_up[0])*60+int(waking_up[1])
        minutes_fap=int(falling_asleep[0])*60+int(falling_asleep[1])
        if minutes_wup<minutes_fap:
            minutes_wup=1440+minutes_wup
        sleep_time=abs(minutes_fap-minutes_wup)

        messages.info(request,f"you will sleep {sleep_time//60} hours and {sleep_time%60} minutes,\n")
    if sleep_time//60>8:
        messages.info(request,"you will sleep enough")
    else:
        messages.info(request,"you will not sleep enough")
    return render(request, 'personal/sleeptracker.html')


def caloriestracker(request):
    if request.method == "POST":
        form = CaloriesTrackerform(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Wrong input'
    form = CaloriesTrackerform()
    error = ''
    contex = {
        'form': form,
        'error': error
    }
    return render(request, 'personal/caloriestracker.html', contex)

