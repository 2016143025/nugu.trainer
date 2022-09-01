from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('write',views.write,name='write'),
    path('like',views.like,name='like'),
    path('wrote',views.wrote,name='wrote')
]