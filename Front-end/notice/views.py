from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'notice.html')

def post(request):
    return render(request, 'post.html')

def content(request):
    return render(request, 'content.html')