

from django.contrib import admin
from django.urls import path
from pybo import views
from django.urls import path, include    # path와 inclue  두 개를 임포트

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')), # pybo/로 시작되는 페이지 요청은 pybo/url.py 파일내용을 참조 처리
    # path('pybo/', views.index),
    path('common/', include('common.urls')),
    path('', views.index, name='index'),  #  루트('/')페이지에 해당하는 것

]
