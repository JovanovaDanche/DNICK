from django.contrib import admin
from .models import Manufacturer, Workshop, Car, Repair, WorkshopManufacturers


# Register your models here.
class WorkshopsManufacturersInlineAdmin(admin.TabularInline):
    model = WorkshopManufacturers
    extra = 1


class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [WorkshopsManufacturersInlineAdmin, ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class RepairAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(RepairAdmin, self).save_model(request, obj, form, change)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False


class CarAdmin(admin.ModelAdmin):
    list_display = ('type', 'maxSpeed',)


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Repair, RepairAdmin)
