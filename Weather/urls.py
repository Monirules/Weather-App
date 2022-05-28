from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name="logout"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('home2', views.home2, name='home2'),
]
