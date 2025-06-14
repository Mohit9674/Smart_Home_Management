from django.urls import path
from .views import TenantListView

app_name = 'tenants'

urlpatterns = [
    path('tenants/', TenantListView.as_view(), name='tenant_list'),
]