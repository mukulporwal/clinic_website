from django.contrib import admin
from indexapp.models import maincarousel, mainbox, difcontent

# Register your models here.
class MainCarouselAdmin(admin.ModelAdmin):
    list_display = ('image',)

admin.site.register(maincarousel, MainCarouselAdmin)

class MainBoxAdmin(admin.ModelAdmin):
    list_display = ('title', 'one_description', 'image_box', 'two_description', 'btnname')

admin.site.register(mainbox, MainBoxAdmin)

class DifContentAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'description')

admin.site.register(difcontent, DifContentAdmin)