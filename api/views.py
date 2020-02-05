from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from jobpost.models import jobs
from providers.models import providers
from seekers.models import jobsheeker
from api.serializers import jobsSerializer, jobsheekerSerializer, providersSerializer


@api_view(['GET',])
def api_details_jobs_view(request):
    try:
        job = jobs.objects.all()
    except jobs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializers = jobsSerializer(job, many=True)
        return Response(serializers.data)


@api_view(['POST',])
def api_create_jobs_view(request):
    job = jobs()
    if request.method == "POST":
        serializer = jobsSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def api_for_company_registration(request):
    provide = providers()
    if request.method == "POST":
        serializer = providersSerializer(provide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def api_for_sheekers_registration(request):
    sheek = jobsheeker()
    if request.method == "POST":
        serializer = jobsheekerSerializer(sheek, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
