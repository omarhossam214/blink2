from django.contrib import admin
from .models import *
# Register your models here.


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['address','customer']


class OrderItemInline(admin.StackedInline):
    model = OrderItem

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress


class OrderInline(admin.ModelAdmin):
    inlines = [OrderItemInline,ShippingAddressInline]
    list_display = ['id', 'customer', 'data_order', 'complete', 'status','cart_total','items_total','total_price','d_fee','promocode','discount_amount','total']
    list_filter = ['complete','status']
    
    
    
    def items_total(self, obj):
        return obj.get_cart_items
    items_total.short_description = 'items Total'



    def cart_total(self, obj):
        if obj.complete == True:
            return '-'
        else:
            return obj.get_cart_total
    cart_total.short_description = 'Cart Total'


    # def save_model(self, request, obj, form, change):
    #     if obj.promocode:
    #         discount_amount = (obj.total * obj.promocode.discount) / 100
    #         obj.total -= discount_amount
    #     obj.save()



admin.site.register(Customer)
admin.site.register(Order,OrderInline)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress,ShippingAddressAdmin)
admin.site.register(Coverage_area)
admin.site.register(Guest)
