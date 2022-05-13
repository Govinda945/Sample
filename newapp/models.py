from django.db import models

country_choice=(
    ('India','India'),
    ('USA','USA'),
    ('China','China'),
    ('Japan','Japan')
)
# Create your models here.0
class Contact(models.Model):
    name= models.CharField(max_length=30)
    dob=models.DateField()
    email=models.EmailField(unique=True)
    phone =models.IntegerField()
    gender=models.CharField( max_length=50)
    flatno=models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    country= models.CharField(choices=country_choice,max_length=50)
    img=models.ImageField(upload_to='about/',blank=True)
