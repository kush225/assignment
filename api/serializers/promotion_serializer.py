from rest_framework import serializers
from api.models.promotions import Promotion

class PromotionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Promotion
		fields = ['id','plan', 'valid_from', 'valid_till', 'max_users_allowed', 'benefitPercentage', 'is_active']


	def validate(self, data):
		valid_from = data['valid_from'] if 'valid_from' in data else None
		valid_till = data['valid_till'] if 'valid_till' in data else None
		if valid_from == None and valid_till == None:
			pass
		else:
			if valid_from == None and valid_till != None:
				raise serializers.ValidationError("Valid from is required with valid till")	
			elif valid_till == None and valid_from != None:
				raise serializers.ValidationError("Valid till is required with valid form")
			if valid_from >= valid_till:
				raise serializers.ValidationError("Valid till date can't be less/equal than valid from.")		

		return data