from django import forms
from django.forms.fields import IntegerField
from django.shortcuts import render
from .models import Distance

class Beta(forms.Form):
    Ingresa = forms.IntegerField(required=False)
    
