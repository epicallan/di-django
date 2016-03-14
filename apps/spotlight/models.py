"""spotlight on a country models such as spotlight on uganda"""
from django.db import models


class Spotlight(models.Model):
	description = models.CharField(max_length=400)
	country = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.description


class Indicators(models.Model):
	name = models.CharField(max_length=100)
	short_description = models.CharField(max_length=120)
	description = models.CharField(max_length=150)
	spotlight = models.ForeignKey(Spotlight, on_delete=models.CASCADE)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.name
