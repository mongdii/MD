from django.contrib import admin
from .models import Openlablist

# Register your models here.
class OpenlabAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

admin.site.register(Openlablist, OpenlabAdmin)