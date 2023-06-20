from django.urls import path
from . import views

app_name = 'privacy_policy'
urlpatterns = [
    path('', views.index, name='index'),
]
