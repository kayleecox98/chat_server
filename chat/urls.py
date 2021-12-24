from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('', views.index, name='index'),
    path('posting/', views.posting, name = 'posting'),
]