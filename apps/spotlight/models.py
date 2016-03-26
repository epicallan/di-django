"""spotlight on a country models such as spotlight on uganda"""
from django.db import models


class Spotlight(models.Model):
	country = models.CharField(max_length=100)
	slug = models.CharField(max_length=100, default='')
	description = models.TextField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.country


class Indicator(models.Model):
	name = models.CharField(max_length=100)
	slug = models.CharField(max_length=120)
	description = models.TextField()
	spotlight = models.ForeignKey(Spotlight, on_delete=models.CASCADE)
	upload = models.FileField(upload_to='uploads/%Y/%m/%d', blank=True, default='')
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.name
