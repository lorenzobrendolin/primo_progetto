"""
URL configuration for primo_progetto project.

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
from django.urls import path
from .views import es_if, if_else_elif, es_for

app_name = "seconda_app"
urlpatterns = [
    path('es_if',es_if,name="es_if"),
    path('if_else_elif',if_else_elif,name="esif_else_elif"),
    path('es_for',es_for,name="es_for"),
    ]
