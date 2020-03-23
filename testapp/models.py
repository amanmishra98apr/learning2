from django.db import models
from django.forms import ModelForm,Textarea
# Create your models here.
class FirstTable(models.Model):
    name=models.CharField(max_length=10);
    branch=models.CharField(max_length=10);
    address=models.CharField(max_length=10);
    marks=models.FloatField(max_length=10);

class Meta:
    db_table="FirstTable"
