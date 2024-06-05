from django.contrib import admin

# Register your models here.
from .models import Supplement

class SupplementAdmin(admin.ModelAdmin):
    list_display = ('name', "category", )

admin.site.register(Supplement, SupplementAdmin)