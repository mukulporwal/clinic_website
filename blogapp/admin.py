from django.contrib import admin
from blogapp.models import blogdata

# Register your models here.
class blogdataAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'description', 'image')

admin.site.register(blogdata, blogdataAdmin)
