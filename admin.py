from django.contrib import admin
from .models import *


# Register your models here.

admin.site.site_header='BLINK administration'
admin.site.site_title="BLINK-administration"

class PhotoAdmin(admin.StackedInline):
    model = Photo


class ProductsAdmin(admin.ModelAdmin):

    list_display = ['Name','price','stock','Category','collection','Color']
    list_display_links = ['Name']
    list_editable = ['stock','price','Category','collection','Color']
    search_fields = ['Name']
    list_filter = ['stock','Category','collection' ,'Color']
    inlines = [PhotoAdmin]

    class Meta:
        model = Products


    

class CategoriesAdmin(admin.ModelAdmin):
    pass
    #list_display = ['Category_name']


class CollectionsAdmin(admin.ModelAdmin):
    pass
    #list_display = ['collection_name']
                         






admin.site.register(Products,ProductsAdmin)
admin.site.register(Collections,CollectionsAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Colors)
admin.site.register(Photo)
