from django.db import models

# Create your models here.

class School(models.Model):
    Sname = models.CharField(max_length = 100,primary_key = True)
    sprinc = models.CharField(max_length = 100)
    sloc = models.CharField(max_length = 100)
    