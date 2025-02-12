import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Corso

# Create your views here.
def index(request):
    return render(request,"index.html")

def view_a(request):
    lista_corsi = Corso.objects.order_by('data_inizio')
    context = {'lista_corsi': lista_corsi}
    return render(request, "view_a.html", context)

def view_b(request, pk):
    corso = Corso.objects.get(pk=pk)
    dettagli = Corso.objects.filter(corso=corso)
    dettagli_corsi = Corso.objects.order_by('data_inizio')
    context = {'dettagli_corsi': dettagli_corsi, 'corso': corso, 'dettagli': dettagli}
    return render(request, "view_b.html", context)  

def view_c(request):
    corsi_dopo = Corso.objects.filter(data_inizio__gt=datetime.date(2025, 5, 1))
    context = {'corsi_dopo': corsi_dopo}
    return render(request, "view_c.html", context)

def view_d(request):
    posti = Corso.objects.filter(posti_disponibili__lte=20)
    context = {'posti': posti}
    return render(request, "view_d.html", context)

def view_e(request):
    corsi_prima = Corso.objects.filter(data_fine__lt=datetime.date(2025, 4, 30))
    context = {'corsi_prima': corsi_prima}
    return render(request, "view_e.html", context)
