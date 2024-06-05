from django.contrib import admin

# Register your models here.
from .models import Balloon, Airline, Pilot, Flight, PilotsAirline


class PilotsAirlineInlineAdmin(admin.TabularInline):
    model = PilotsAirline
    extra = 1


class BalloonAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PilotAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname',)


class AirlineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [PilotsAirlineInlineAdmin, ]

class FlightAdmin(admin.ModelAdmin):
    exclude = ("user", )
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(FlightAdmin, self).save_model(request, obj, form, change)
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Pilot, PilotAdmin)
admin.site.register(Flight,FlightAdmin)
