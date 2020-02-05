from django.contrib import admin
from providers.models import providers
# Register your models here.
class providersAdmin(admin.ModelAdmin):
    list_display=['UserName', 'FirstName', 'LastName','Email_ID','Address', 'PhoneNumber', 'Requirement', 'Company']


admin.site.register(providers, providersAdmin)
