from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import ValidationError
from api.models.brands import Brand


BENEFIT_TYPE_CHOICES = [
    ("cashback", "cashback"),
    ("extraVoucher", "extraVoucher"),
]

class Plan(models.Model):
	"""class representing plan entity"""
	planID = models.AutoField(primary_key=True)
	planName = models.CharField(max_length=50)
	amount_min = models.FloatField(validators=[MinValueValidator(1000.0)] )
	amount_max = models.FloatField(validators=[MaxValueValidator(500000.0)])
	tenure_min = models.IntegerField(validators=[MinValueValidator(3)])
	tenure_max = models.IntegerField(validators=[MaxValueValidator(11)])
	benefitPercentage = models.FloatField(default=0, validators=[MinValueValidator(1.0), MaxValueValidator(99.0)])
	benefitType = models.CharField(max_length=30, choices=BENEFIT_TYPE_CHOICES, default=BENEFIT_TYPE_CHOICES[0][0])
	createAt = models.DateTimeField(auto_now_add=True)
	brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.CASCADE)

