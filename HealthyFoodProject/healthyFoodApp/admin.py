from django.contrib import admin
from .models import Client, Category, Product, Order


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class CategoryAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request,obj=None):
        if request.user.is_superuser:
            return True
        return False

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name","surname",)


admin.site.register(Client,ClientAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
