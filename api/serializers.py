from rest_framework import serializers
from jobpost.models import jobs
from seekers.models import jobsheeker
from providers.models import providers


class jobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobs
        fields = [ 'jobtitle','company','location', 'requirements']


class jobsheekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobsheeker
        fields = ['UserName', 'FirstName','LastName', 'Email_ID', 'Address', 'PhoneNumber', 'Image', 'Qualifications']


class providersSerializer(serializers.ModelSerializer):
    class Meta:
        model = providers
        fields = ['UserName', 'FirstName','LastName', 'Email_ID', 'Address', 'PhoneNumber', 'Image', 'Requirement', 'Company']
