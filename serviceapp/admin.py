from django.contrib import admin
from serviceapp.models import fertiService, endometriosis, laparoscopy, riskdelivery

# Register your models here.
class FertiServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'btnname', 'image', 'description')


admin.site.register(fertiService, FertiServiceAdmin)

class EndometriosisAdmin(admin.ModelAdmin):
    list_display = ('name', 'btnname', 'image', 'description')

admin.site.register(endometriosis, EndometriosisAdmin)

class LaparoscopyAdmin(admin.ModelAdmin):
    list_display = ('name', 'btnname', 'image', 'description')

admin.site.register(laparoscopy, LaparoscopyAdmin)

class RiskDeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'btnname', 'image', 'description')

admin.site.register(riskdelivery, RiskDeliveryAdmin)