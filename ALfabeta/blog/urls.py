from django.urls import path
from blog import views
from django.conf import settings

urlpatterns =[
    path('',views.index,name='index'),
    path('registrou',views.registrou,name='index')
]