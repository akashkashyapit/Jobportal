from django.db import models

# Create your models here.
class jobs(models.Model):
    jobtitle=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    location=models.CharField(max_length=64)
    requirements=models.CharField(max_length=1000)
