from django.shortcuts import render
from .models import Distance
from .forms import Beta

# Create your views here.
def grafo(request):
    template_name = "grafo/grafo.html"
    form = Beta(request.POST)
    if form.is_valid():
        umbral = form.cleaned_data['Ingresa']
        form = Beta()
    L=Distance.objects.get_queryset()
    diccionario = {'umbral':umbral, 'form':form, 'lista':L}
    return render(request, template_name, diccionario)

""" def arreglo(lista):
    row=[]
    for i in lista:
        col=[]
        for j in lista:
            suma=0
            suma=suma+((i.temperatura-j.temperatura)**2)+((i.color-j.color)**2)+((i.inflammation-j.inflammation)**2)
            dist=suma**0.5
            col.append(dist)
        row.append(col)
    return row """