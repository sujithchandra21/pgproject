from django.db import models

# Create your models here.
class PG(models.Model):
    pg_code = models.CharField(primary_key=True,max_length=10)
    pg_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    rating = models.FloatField()

class Status_PG(models.Model):
    pg_id = models.ForeignKey(PG,on_delete=models.CASCADE)
    sharing = models.CharField(max_length = 25)
    price = models.IntegerField()
    total_strength = models.IntegerField()
    vaccancies = models.IntegerField()
    images = models.ImageField(upload_to='images/')
    
class Registration_PG(models.Model):
    Registration_id = models.CharField(primary_key=True,max_length = 10)
    Full_name = models.CharField(max_length = 25)
    Email = models.CharField(max_length = 50)
    Mobile_number = models.CharField(max_length = 10)
    sharing_person = models.CharField(max_length=25,null=True)
    price_person = models.IntegerField(null=True)
