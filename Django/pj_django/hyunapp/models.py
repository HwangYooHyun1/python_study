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

class Member(models.Model):
	name = models.CharField(max_length=30)
	email = models.TextField(primary_key=True) #id필드가 따로 생성되지 않게 함
	pwd = models.CharField(max_length=30)
	phone = models.CharField(max_length=50)
	rdate = models.DateTimeField() #등록 date
	udate = models.DateTimeField() #update date
 