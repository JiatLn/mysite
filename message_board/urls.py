from django.urls import path

from . import views


# start with message
urlpatterns = [
    path('', views.message, name='message'),
]