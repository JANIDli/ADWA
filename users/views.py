from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from .form import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('please enter valide username')

        user = authenticate(req, username=username, password=password)
        
        if user is not None:
            login(req, user)
            return redirect('home')
        else:
            print('wrong username or password')


    return render(req, 'users/login.html')



def user_register(req):
    if req.user.is_authenticated:
        return redirect('home')
    form = UserRegisterForm()
    if req.method == "POST":
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(req, user)
            return redirect('home')
        
    context = {'form':form}
    return render(req, 'users/register.html', context)



def user_logout(req):
    logout(req)
    return redirect('home')
