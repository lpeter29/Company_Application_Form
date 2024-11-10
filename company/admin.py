from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'region', 'city')  # Fields to display in the list view
    search_fields = ('name', 'type', 'city')  # Fields to search by
    list_filter = ('type', 'region')  # Filters for the admin interface

admin.site.register(Company, CompanyAdmin)
