from django.urls import path
from .views import contatti, elimina_contatto, listacontatti, modifica_contatto

app_name = 'forms_app'

urlpatterns = [
    path('contatti/', contatti, name='contatti'),
    path('lista/', listacontatti, name='listacontatti'),
    path('elimina/<int:id>/', elimina_contatto, name='elimina_contatto'),
    path('modifica/<int:id>/', modifica_contatto, name='modifica_contatto'),
]
