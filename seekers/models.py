from django.db import models

# Create your models here.
class jobsheeker(models.Model):
    UserName=models.CharField(max_length=64)
    FirstName=models.CharField(max_length=64)
    LastName=models.CharField(max_length=64)
    Email_ID=models.EmailField()
    Address=models.CharField(max_length=64)
    PhoneNumber=models.IntegerField()
    Image=models.ImageField(upload_to="providers/images", default="")
    Qualifications=models.CharField(max_length=100)
