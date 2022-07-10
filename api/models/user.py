from django.db import models
from django.contrib.auth.models import AbstractUser

TYPE_CHOICES = [
	("customer", "customer"),
   	("merchant", "merchant"),
]

class User(AbstractUser):
	type = models.CharField(max_length=20, choices=TYPE_CHOICES)

	# USERNAME_FIELD = 'username'
	# REQUIRED_FIELDS = ['email']

	# def __str__(self):
	# 	return self.username

	# def create_user(self, email, date_of_birth, password=None):
	# 	"""
	# 	Creates and saves a User with the given email, date of
	# 	birth and password.
	# 	"""
	# 	if not email:
	# 		raise ValueError('Users must have an email address')

	# 	user = self.model(
	# 	email=self.normalize_email(email),
	# 	date_of_birth=date_of_birth,
	# 	)

	# 	user.set_password(password)
	# 	user.save(using=self._db)
	# 	return user

	# def create_superuser(self, email, date_of_birth, password):
	# 	"""
	# 	Creates and saves a superuser with the given email, date of
	# 	birth and password.
	# 	"""
	# 	user = self.create_user(email,
	# 	password=password,
	# 	date_of_birth=date_of_birth
	# 	)
	# 	user.is_admin = True
	# 	user.save(using=self._db)
	# 	return user