from django.urls import path

import adminapp.views as adminapp


app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('users/', adminapp.UserListView.as_view(), name='admin_users'),
    # path('users/', adminapp.admin_users, name='admin_users'),
    # path('users/create/', adminapp.admin_users_create, name='admin_users_create'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', adminapp.UserDeleteView.as_view(), name='admin_users_remove'),
    # path('categories/', adminapp.categories, name='categories'),
    # path('logout/', adminapp.logout, name='logout'),

]