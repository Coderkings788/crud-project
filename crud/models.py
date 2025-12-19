from django.db import models

class rform(models.Model):
    genderchoice=[
        ('M',"Male"),
        ('F',"Female")
    ]
    fname=models.CharField(max_length=15)
    lname=models.CharField(max_length=15)
    dob=models.DateField()
    gender=models.CharField(max_length=1, choices=genderchoice)
    file=models.FileField(upload_to='User_image/',null=True,blank=True)

# Create your models here.
