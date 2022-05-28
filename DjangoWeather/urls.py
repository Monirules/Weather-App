"""DjangoWeather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.conf.urls.static import static
from Weather import views
from django.contrib import admin
from django.urls import include, path
from DjangoWeather import settings
from . import urls
from django.contrib import admin

admin.site.site_title = 'Weather App Admin'
admin.site.site_header = 'Weather App Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('logout', views.logout, name="logout"),
    path('home2', views.home2, name='home2'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
