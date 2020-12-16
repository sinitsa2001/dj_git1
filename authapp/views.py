from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm


def login(request):
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(username=username, password =password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main')) #index

    context = {'form':form}
    return render(request, 'authapp/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()

    context = {'form':form}
    return render(request, 'authapp/register.html', context)

def logout (request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


