from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from basketapp.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()
        # messages.error(request,print(form.errors))

    context = {'form':form}
    return render(request, 'authapp/register.html', context,print(form.errors))

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    baskets = Basket.objects.filter(user=request.user)

    # total_quantity = 0
    # for basket in Basket.objects.filter(user=request.user):
    #     total_quantity += basket.quantity
    #
    # total_sum =0
    # for basket in Basket.objects.filter(user=request.user):
    #     total_sum += basket.sum()



    context = {
            'form':form,
            'baskets': baskets,
            # 'total_quantity':sum(basket.quantity for basket in baskets),
            # 'total_sum': sum(basket.sum() for basket in baskets),
                   }
    return render(request,'authapp/profile.html',context)



def logout (request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


