from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

# Create your views here.



def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
        return render(request, 'loginuser.html', {'form': AuthenticationForm(), 'error': 'Логин и/или пароль не найдены!'})
    else:
        login(request, user)
        return redirect('home') 


def signup(request):
  # if request.method == 'POST': тут почему-то ошибка...
    user_form=SignupForm(request.POST)
    if user_form.is_valid():
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password1'])
      new_user.save()
      return render(request, 'signup.html',{'new_user':new_user})
    else:
      user_form = SignupForm()
      
    return render(request, 'signup.html', {'user_form':user_form}) #{'user_form':user_form}