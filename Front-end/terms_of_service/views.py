from django.shortcuts import render


def index(request):
    return render(request, 'terms_of_service.html')