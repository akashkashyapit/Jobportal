from django.contrib import admin
from jobpost.models import jobs
# Register your models here.
class jobsAdmin(admin.ModelAdmin):
    list_display=['jobtitle', 'company', 'requirements','location']


admin.site.register(jobs, jobsAdmin)
