
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload, name='upload'),
    path('download/<str:file>', views.download, name='download'),
]
