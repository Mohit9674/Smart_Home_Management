from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Property

class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'
    
class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property_detail.html'
    context_object_name = 'property'    