from django.urls import path
from .views import index

app_name = "corsi_formazione"
urlpatterns = [
    path('index',index,name="index"),
    ]
