from django.contrib import admin
from .models import Room, RoomEmployee, Reservation, Employee
from django.core.exceptions import ValidationError


# Register your models here.
class RoomEmployeeInlineAdmin(admin.TabularInline):
    model = RoomEmployee
    extra = 1

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'employees':
            kwargs['queryset'] = Employee.objects.filter(type='H')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('num', 'is_clean',)
    inlines = [RoomEmployeeInlineAdmin, ]

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj:
            try:
                employee = obj.roomemployee_set.first().employees
                if employee.type == 'H':
                    return True
            except AttributeError:
                pass
        return False



class ReservationAdmin(admin.ModelAdmin):
    list_display = ('code', 'room',)
    exclude = ("user",)
    def save_model(self, request, obj, form, change):
        # Check if the room is clean before saving
        if not obj.room.is_clean:
            raise ValidationError('The room must be clean before making a reservation.')
        obj.user = request.user
        return super(ReservationAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(Room, RoomAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Employee)
