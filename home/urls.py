from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('<str:slug>',views.home_detail,name='detail'),
]
