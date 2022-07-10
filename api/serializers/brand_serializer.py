from rest_framework import serializers
from api.models.brands import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'description'] 