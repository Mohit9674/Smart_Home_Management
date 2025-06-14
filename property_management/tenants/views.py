from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Tenant

class TenantListView(ListView):
    model = Tenant
    template_name = 'tenants/tenant_list.html'
    context_object_name = 'tenants'