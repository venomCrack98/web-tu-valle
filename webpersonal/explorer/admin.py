from django.contrib import admin
from .models import Explorer
# Register your models here.
class ExplorerAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Explorer, ExplorerAdmin) 

