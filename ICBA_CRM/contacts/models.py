from django.db import models

# Create your models here.

class Organization(models.Model):
    Name = models.CharField(max_length=100, null=False)
    Category = models.CharField(max_length=200, null=False)
    Address = models.CharField(max_length=100)
    Website = models.URLField()
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.Name

class Contact(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email = models.EmailField(unique=True)
    Phone_Number = models.CharField(max_length=15, unique=True)
    designation = models.CharField(max_length=60)
    Organizations = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL)


class Menu(models.Model):
    title = models.CharField(max_length=40)
    link = models.CharField(max_length=1041)
    alt = models.CharField(max_length=100)