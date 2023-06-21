from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    path('privacy_policy/', include("privacy_policy.urls")),
    path('terms_of_service/', include("terms_of_service.urls")),
    path('join/',include('join.urls')), # 회원가입
    path('home/',include('home.urls')), # 홈
    path('notice/',include('notice.urls')), # 공지사항
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)