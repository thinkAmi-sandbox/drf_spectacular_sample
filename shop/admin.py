from django.contrib import admin

from shop.models import Shop


# Register your models here.
class ShopModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'size', 'established_at', 'updated_at')


admin.site.register(Shop, ShopModelAdmin)
