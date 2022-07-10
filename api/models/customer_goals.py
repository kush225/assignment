from django.db import models
from api.models.brands import Brand
from api.models.plans import Plan
from api.models.promotions import Promotion
from django.core.validators import MaxValueValidator, MinValueValidator
from api.models.user import User

BENEFIT_TYPE_CHOICES = [
    ("cashback", "cashback"),
    ("extraVoucher", "extraVoucher"),
]


class CustomerGoal(models.Model):
	"""class representing CustomerGoal entity"""
	id = models.AutoField(primary_key=True)
	brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
	plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
	promotion = models.ForeignKey(Promotion, on_delete=models.PROTECT)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	selectedAmount = models.IntegerField(validators=[MinValueValidator(1000.0), MaxValueValidator(500000.0)])
	selectedTenure = models.IntegerField(validators=[MinValueValidator(3), MaxValueValidator(11)])
	startDate = models.DateField(auto_now_add=True)
	depositedAmount = models.IntegerField()
	benefitPercentage = models.IntegerField()
	createAt = models.DateTimeField(auto_now_add=True)
	benefitType = models.CharField(max_length=30, choices=BENEFIT_TYPE_CHOICES, default=BENEFIT_TYPE_CHOICES[0][0])
