from rest_framework import serializers
from api.models.plans import Plan

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['planID', 'planName', 'amount_min', 'amount_max', 'tenure_min', 'tenure_max', 'benefitType', 'brand']

    def validate(self, data):
        # amount validation
        amount_min = data['amount_min']
        amount_max = data['amount_max']
        if amount_min >= amount_max:
            raise serializers.ValidationError("Minimum amount should be lesser than maximum amount.")

        # tenure validation
        tenure_min = data['tenure_min']
        tenure_max = data['tenure_max']
        
        if tenure_min >= tenure_max:
            raise serializers.ValidationError("Minimum tenure should be lesser than maximum tenure.")

        return data