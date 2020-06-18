from django.db import models

# Create your models here.

class Organization(models.Model):
    Name = models.CharField(max_length=100)
    Category = models.CharField(max_length=200)
    Address = models.CharField(max_length=100)
    Website = models.URLField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=15)

    def __str__(self):
        return self.Name

class Contact(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=15)
    designation = models.CharField(max_length=60)
    Organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)


class Menu(models.Model):
    title = models.CharField(max_length=40)
    link = models.CharField(max_length=1041)
    alt = models.CharField(max_length=100)