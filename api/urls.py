from django.urls import path
from api.views import api_details_jobs_view, api_create_jobs_view, api_for_company_registration, api_for_sheekers_registration

app_name = 'jobpost'

urlpatterns = [
path('job-list',api_details_jobs_view, name = "details"),
path('create-job',api_create_jobs_view, name = 'create-job'),
path('company-registration',api_for_company_registration, name = 'company-registration'),
path('sheekers-registration',api_for_sheekers_registration, name = 'sheekers-registration'),
]
