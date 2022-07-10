from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from api.models.user import User

class Brand(models.Model):
	"""class representing brand entity"""
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	description = models.TextField(max_length=500, blank=True, null=True)
	createAt = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)