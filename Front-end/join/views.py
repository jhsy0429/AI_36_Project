from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'join_terms.html')

def join(request):
    return render(request, 'join.html')