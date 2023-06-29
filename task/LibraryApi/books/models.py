from django.db import models

class Book(models.Model):
    Title=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Publication_Year = models.IntegerField()