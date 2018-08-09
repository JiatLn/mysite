from django.urls import path

from . import views


# start with blog
urlpatterns = [
    path('login_for_modal/', views.login_for_modal, name='login_for_modal'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('info/', views.user_info, name='info'),
]