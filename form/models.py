from django.db import models

# Create your models here.
from django.utils import timezone
from datetime import date

class User(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=100, null=False)
	Fname = models.CharField(max_length=100, null=False)
	Lname = models.CharField(max_length=100, null=False)
	passHash = models.CharField(max_length=255, null=False)
	

	def __str__(self):
		data = [self.id,self.email,self.passHash, self.Fname. self.Lname]
		return data

class Event(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100,null=False)
	userID = models.ForeignKey(User, on_delete=models.CASCADE)	
		
	def __str__(self):
		data = [self.id,self.userID,self.name]
		return data

class EventDetails(models.Model):
	id = models.AutoField(primary_key=True)
	eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
	name = models.CharField(max_length=100,null=False)
	jsondata = models.TextField(null=False)
	date_create = models.DateField(("Date_Create"), auto_now_add=True)
	last_modified = models.DateField(("Last_Modified"), auto_now=True)
	
	def __str__(self):
		data = [self.id,self.name,self.jsondata, self.date_create, self.last_modified, self.eventID]
		return data

class Response(models.Model):
	id = models.AutoField(primary_key=True)
	eventID = models.ForeignKey(Event, on_delete=models.CASCADE)
	eventDetailsID = models.ForeignKey(EventDetails, on_delete=models.CASCADE)
	responseJSON = models.TextField(null=False)
	imagePath = models.TextField(null=False)
	idCardPath = models.TextField(null=False)
	date = models.DateField(("Date"), auto_now_add=True)

	def __str__(self):
		data = [self.id, self.eventID, self.eventDetailsID,self.responseJSON,self.imagePath,self.idCardPath]
		return data

