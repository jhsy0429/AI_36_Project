from django.urls import path
from . import views

app_name = 'terms_of_service'
urlpatterns = [
    path('', views.index, name='index'),
]
