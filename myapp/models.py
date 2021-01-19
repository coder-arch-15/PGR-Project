from django.db import models

# Create your models here.
class user(models.Model):

   name = models.CharField(max_length = 50)
   mail = models.EmailField()
   addr = models.CharField(max_length = 100)
   phone = models.IntegerField()
   dob = models.DateField()
   gender = models.CharField(max_length = 6)
   password = models.CharField(max_length = 15, default = "1234test")
   pending = models.IntegerField(default = 1)
   approved = models.IntegerField(default = 0)

   class meta(object):
   	db_table = "user"
   		
