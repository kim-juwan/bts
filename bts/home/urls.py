from django.urls import path

from . import views   # 현재 패키지에서 views 모듈을 가져옴

urlpatterns = [
    path('', views.home, name='home'),
    path('ppt1',views.ppt1,name='ppt1'),
    path('ppt2',views.ppt2,name='ppt2'),

]