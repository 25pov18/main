from django.contrib import admin
from zakaz.models import adres, zakaz
# Register your models here.

class zakazInLine(admin.StackedInline):
       model = adres
       extra = 2

class zakazAdmin(admin.ModelAdmin):
       inlines = [zakazInLine]
       list_filter = ['data_time']


admin.site.register(zakaz,zakazAdmin)
