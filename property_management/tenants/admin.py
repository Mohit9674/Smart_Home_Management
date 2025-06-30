from django.contrib import admin
from .models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'property',        # not property_address
        'full_name',
        'email',
        'smoker',          # not is_smoker
        'current_income',  # not current_in
        'license_fee',
        'deposit',
    )
    list_filter = (
        'smoker',
        'current_income',
    )
    search_fields = (
        'full_name',
        'email',
        'property',
    )
