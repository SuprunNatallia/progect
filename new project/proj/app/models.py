from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Massages(models.Model):
    service = models.CharField(max_length=250)
    price = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.service} {self.price}"

class Cosmetolog(models.Model):
    service = models.CharField(max_length=250)
    price = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.service} {self.price}"

class Specialists(models.Model):
    photo = models.ImageField(upload_to='uploads')
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    additional = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Client(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True, blank=False)
    text = models.TextField(blank=False)
    issued = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.email}"
