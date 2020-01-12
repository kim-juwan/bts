from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴

urlpatterns = [
    path('', views.home, name='home'),
    path('index',views.index,name='index'),
    path('index2',views.index2,name='index2'),

]