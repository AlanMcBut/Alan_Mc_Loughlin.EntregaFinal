from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
]