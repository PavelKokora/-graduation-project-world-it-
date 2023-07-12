"""SeriesZone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import settings
from django.conf.urls.static import static
from authorization.views import *
from catalog.views import *
from user_page.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_reg, name='registration'),
    path('auth/', view_auth, name='login'),
    path('search/', view_search, name='search'),
    path('catalog/', view_catalog, name='catalog'),
    path('catalog/<int:serial_pk>/', view_serial, name="serial_view"),
    path('user/' , view_user , name="profile"),
    path('buy/<int:serial_pk>/', view_form, name='buy_form')
    
] + static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
