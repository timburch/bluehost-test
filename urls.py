from django.urls import path

from . import views

print('urls.py')

urlpatterns = [
    path('', views.list, name='list'),
    path('add', views.add, name='add'),
    path('load', views.load, name='load'),
    path('email', views.email, name='email')
]
