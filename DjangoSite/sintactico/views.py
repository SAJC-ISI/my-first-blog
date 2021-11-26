from django.shortcuts import render
from home.models import Tessiu

# Create your views here.
def sintactico (request):
    L=Tessiu.objects.get_queryset()
    template_name = "sintactico/sintactico.html"
    diccionario = {'lista':L}
    return render(request, template_name, diccionario)
    