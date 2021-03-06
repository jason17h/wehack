"""enghack2019 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from hackerhub import views, send_sms
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('hackerhub/', include('hackerhub.urls')),
    path('portal/<eventId>/', views.portal, name='portal'),
    path('portal/<eventId>/resources/', views.resources, name='resources'),
    path('sms', send_sms.sendSMS, name='sms'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

