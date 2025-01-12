from django.contrib import admin
from . import models
# Register your models here.
class chaireviewinline(admin.TabularInline):
    model = models.chaireview  
    extra = 2 #if required we can add 2 reviews at once in the admin panel 


class chaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name','type','date_added')
    inlines = [chaireviewinline] #


class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_name','location')
    filter_horizontal=('chai_variety',)

class chaicertificateAdmin(admin.ModelAdmin):
    list_display = ('chai','certificate_number','issue_date','valid_until')



admin.site.register(models.chaiVariety, chaiVarietyAdmin)
admin.site.register(models.Store, StoreAdmin)
admin.site.register(models.chaiCertificate, chaicertificateAdmin)

