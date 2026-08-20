from django.contrib import admin
from .models import CustomUser, Country

class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'country',
        'is_staff',
        'is_active',
    )

class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

    search_fields = (
        'name',
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Country, CountryAdmin)

