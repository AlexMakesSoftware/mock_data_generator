from django.contrib import admin

from .models import *

class FarmInline(admin.StackedInline):    
    model = Farm
    extra = 0    

class OwnerAdmin(admin.ModelAdmin):
    inlines = [FarmInline]
    list_per_page = 20

class IncidentAdmin(admin.ModelAdmin):
    model=Incident
    list_per_page = 20
    list_display = ('incident_number', 'start_date', 'end_date', 'status', 'farm')
    search_fields = ('incident_number', 'start_date', 'end_date')
    

class FarmsAdmin(admin.ModelAdmin):
    model=Farm
    list_per_page = 20

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Farm, FarmsAdmin)
admin.site.register(Incident, IncidentAdmin)

