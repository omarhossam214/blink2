from django.contrib import admin
from .models import *
from django.forms.models import inlineformset_factory
from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder
import datetime


# Register your models here.

admin.site.site_header='BLINK administration'
admin.site.site_title="BLINK-administration"






class CollectionInline(admin.TabularInline):
    model = Products.collection.through
    extra = 0
    can_delete = True




class PhotoAdmin(admin.StackedInline):
    model = Photo
    extra = 0




class StockoInline(admin.StackedInline):
    model = Stocko
    extra = 1



class ProductsAdmin(admin.ModelAdmin):
    list_display = ['Name','price','old_price','stock','Category','Color','total_quantity',]
    list_display_links = ['Name']
    list_editable = ['stock','price','Category','Color','old_price']
    search_fields = ['Name']
    list_filter = ['stock','Category','Color',("data_order", DateRangeFilterBuilder()),]
    inlines = [CollectionInline,PhotoAdmin,StockoInline]
    exclude = ('collection',)
    readonly_fields = ('total_quantity',)

    # class Meta:
    #     model = Products

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     if change:
    #         stock = Stocko.objects.get(product=obj)
    #     else:
    #         stock = Stocko(product=obj)
    #     stock.save()


    

class CategoriesAdmin(admin.ModelAdmin):
    pass
    #list_display = ['Category_name']


                         

class StockoAdmin(admin.ModelAdmin):

    list_display = ['product','S_count','L_count','XL_count','XXL_count']
    list_display_links = ['product']
   
    








admin.site.register(Products,ProductsAdmin)
admin.site.register(Collections)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Colors)
admin.site.register(Stocko,StockoAdmin)
admin.site.register(PromoCode)

