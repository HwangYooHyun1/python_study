from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=200)
    addr = models.TextField()
    rdate = models.DateTimeField()
    

class BoardAddress(models.Model):
    writer = models.CharField(max_length=200)
    email = models.TextField()
    subject = models.TextField()
    content = models.TextField()
    rdate = models.DateTimeField()
