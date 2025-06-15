from django.urls import path
from .views import TenantListView

app_name = 'tenants'

urlpatterns = [
    # List view now at root of this app
    path('', TenantListView.as_view(), name='tenant_list'),
]