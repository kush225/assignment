from django.db import models
from django.forms import ValidationError
from api.models.plans import Plan
from datetime import date, timedelta
from django.core.validators import MaxValueValidator, MinValueValidator


def get_deadline():
    return date.today() + timedelta(days=30)

def min_date(value):
    today = date.today()
    if value < today:
        raise ValidationError('Valid from cannot be in the past.')

class Promotion(models.Model):
	"""class representing promotion entity"""
	id = models.AutoField(primary_key=True)
	plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
	valid_from = models.DateField(default=None, validators=[min_date],null=True)
	valid_till = models.DateField(default=None,null=True)
	max_users_allowed = models.IntegerField(default=0,validators=[MinValueValidator(0)]) # no user limit in case of 0
	users_enrolled = models.IntegerField(null=True,default=0)
	benefitPercentage = models.IntegerField(default=10, validators=[MinValueValidator(1.0), MaxValueValidator(99.0)])
	createAt = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if self.is_active:
			# select all other active items
			qs = type(self).objects.filter(is_active=True, plan_id = self.plan_id)
			# except self (if self already exists)
			if self.pk:
				qs = qs.exclude(pk=self.pk)
			# and deactive them
			qs.update(is_active=False)
			# update plan benefit percentage to active promotion benefit percentage.
			Plan.objects.filter(pk=self.plan_id).update(benefitPercentage=self.benefitPercentage)

		super(Promotion, self).save(*args, **kwargs)