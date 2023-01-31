from django.db import models

class ApiModel(models.Model):
	category = models.CharField(max_length=255)
	subcategeory = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	amount = models.PositiveIntegerField()

	def __str__(self): 
		return self.name




