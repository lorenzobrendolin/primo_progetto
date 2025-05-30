from django.urls import path
from .views import home, articoloDetailView, listaArticoli, queryBase

app_name = 'news'

urlpatterns = [
    path('', home, name="homepage"),
    path('articoli/<int:pk>', articoloDetailView, name="articolo_detail"),
    path('lista_articoli/', listaArticoli, name="lista_articoli"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli"),
    path('query_base/', queryBase, name="query_base"),
]
