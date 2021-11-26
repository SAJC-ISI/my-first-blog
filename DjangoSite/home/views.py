from django.shortcuts import render
from .models import Tessiu

# Create your views here.
def home(request):
    L=Tessiu.objects.get_queryset()
    template_name = "home/index.html"
    diccionario = {'lista':L}
    return render(request, template_name, diccionario)