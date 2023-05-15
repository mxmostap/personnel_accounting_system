from django.contrib import messages
from django.contrib.auth import authenticate
from django.db import DatabaseError
from django.shortcuts import render, redirect

from staff.forms import RegisterUserForm, AuthorizationForm


# Create your views here.

def home(request):
    return render(request, 'staff/home.html')

def registration(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # можно добавить автоматическую аутентификацию пользователя здесь
            return redirect('home')
        else:
            messages.error(request, 'Вы ввели некорректные данные, повторите ввод!')
            return render(request, 'staff/registration.html', {'form': form})
    else:
        form = RegisterUserForm()
    return render(request, 'staff/registration.html', {'form': form})

def authorization(request):
    if request.method == 'POST':
        form = AuthorizationForm(data=request.POST)
        if form.is_valid():
            # аутентификация пользователя
            # ...
            return redirect('home')
        else:
            messages.error(request, 'Вы ввели некорректные данные, повторите ввод!')
            return render(request, 'staff/authorization.html', {'form': form})
    else:
        form = AuthorizationForm()
    return render(request, 'staff/authorization.html', {'form': form})

# def logout(request):
#     if request.method == 'POST':
#         form = AuthorizationForm(data=request.POST)
#         if form.is_valid():
#             # аутентификация пользователя
#             # ...
#             return redirect('home')
#         else:
#             messages.error(request, 'Вы ввели некорректные данные, повторите ввод!')
#             return render(request, 'staff/authorization.html', {'form': form})
#     else:
#         form = AuthorizationForm()
#     return render(request, 'staff/authorization.html', {'form': form})
