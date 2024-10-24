from django.urls import path

from .views import register_page_view


urlpatterns = [
    path('register/', register_page_view, name='register'),
]
