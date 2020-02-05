from django.contrib import admin
from seekers.models import jobsheeker
# Register your models here.
class jobsheekerAdmin(admin.ModelAdmin):
    list_display=['UserName', 'FirstName', 'LastName','Email_ID','Address', 'PhoneNumber', 'Qualifications']


admin.site.register(jobsheeker, jobsheekerAdmin)
