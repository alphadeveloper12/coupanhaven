"""
URL configuration for coupans project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from web.views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('stores/', stores, name="stores"),
    path('category/', category, name="category"),
    path('coupans/', coupans, name="coupans"),
    path('dealCoupans/', dealCoupans, name="dealCoupans"),
    path('blog/', blog, name="blog"),
    path('stores/store_detail/<int:pk>/', store_details, name='store-detail'),
    path('aboutUs/', about_us, name='about-us'),
    path('privacy_policy/', privacy_policy, name='privacy-policy'),
    path('contact_us/', contact_us, name='contact-us'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
