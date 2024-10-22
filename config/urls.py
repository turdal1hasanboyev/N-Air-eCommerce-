"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

### handler 404 ni import qilish
from django.conf.urls import handler404

### page_not_found ni chaqirish yoki to'g'ridan to'g'ri bersa ham bo'ladi

'''
config.errors.custom_page_not_found_page_view
'''
### qilib

from .errors import custom_page_not_found_page_view

urlpatterns = [
    # admin panel
    path('n_air/', admin.site.urls),

    ### ckeditor path
    path('ckeditor/', include('ckeditor_uploader.urls')),

    ### local path
    path('', include('apps.common.urls')),
    path('', include('apps.n_air.urls')),
    path('', include('apps.contact.urls')),
    path('', include('apps.user.urls')),

    ### re_path path (STATIC_ROOT va MEDIA_ROOT ni ko'rsatish uchun) DEBUG False bo'lsa faqat local da ishlaydi
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

### DEBUG False bo'lsa ushbu view ishga tushadi
handler404 = custom_page_not_found_page_view

### DEBUG True holatda (STATIC_ROOT va MEDIA_ROOT ni ko'rsatish uchun) faqat local uchun
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
