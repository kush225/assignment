from django.forms import ValidationError
from rest_framework import serializers
from api.models.customer_goals import CustomerGoal
from api.models.promotions import Promotion
from datetime import date

class CustomerGoalSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerGoal
		fields = '__all__'

class CustomerGoalCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerGoal
		fields = ['plan', 'selectedAmount', 'selectedTenure' ]

	def validate(self, data):
		plan = data['plan']
		selectedAmount = data['selectedAmount']
		selectedTenure = data['selectedTenure']
		if selectedAmount > plan.amount_max or selectedAmount < plan.amount_min:
			raise serializers.ValidationError("Selected amount doesn't meet the plan requirement")

		if selectedTenure > plan.tenure_max or selectedAmount < plan.tenure_min:
			raise serializers.ValidationError("Selected tenure doesn't meet the plan requirement")

		promotion = Promotion.objects.filter(plan_id = plan.pk, is_active=True).last()

		if promotion == None:
			print(1)
			raise ValidationError('Selected plan has no active promotions.') 	

		#date validation 
		if promotion.valid_from == None or promotion.valid_till == None:
			pass
		else:
			today = date.today()
			if today < promotion.valid_from or today >= promotion.valid_till:
				print(2, today, promotion.valid_from, promotion.valid_till)
				raise ValidationError('Selected plan has no active promotions.') 

		# user limit validation
		if promotion.max_users_allowed != 0:
			if promotion.users_enrolled >= promotion.max_users_allowed:
				print(3)
				raise ValidationError('Selected plan has no active promotions.') 
		return data