from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm,UserAdminProfileForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'adminapp/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:admin_users'))
        # else:
        #     print(form.errors)
    else:
        form = UserAdminRegisterForm()
        # messages.error(request,print(form.errors))

    context = {'form':form}
    return render(request, 'adminapp/admin-users-create.html', context,print(form.errors))

@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    user = User.objects.get(id =user_id)

    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)
    # baskets = Basket.objects.filter(user=request.user)
    context = {'form':form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html',context)

@user_passes_test(lambda u: u.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    # user.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))
