from django.urls import path
from .views import PropertyListView

app_name = 'properties'

urlpatterns = [
    path('properties/', PropertyListView.as_view(), name='property_list'),
]