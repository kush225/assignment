from api.models.brands import Brand
from api.models.plans import Plan
from api.permissions.userPermission import IsBrandUser
from api.serializers.brand_serializer import BrandSerializer
from django.http import Http404
from api.serializers.plan_serializer import PlanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema


class BrandCreate(generics.CreateAPIView):
	model = Brand
	serializer_class = BrandSerializer
	queryset = Brand.objects.all()
	permission_classes = [IsBrandUser]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	@swagger_auto_schema(tags=["Brand"])
	def post(self, request, *args, **kwargs):
		"""
		Add a brand
		"""
		return self.create(request, *args, **kwargs)


class BrandList(generics.ListAPIView):	
	model = Brand
	serializer_class = BrandSerializer
	queryset = Brand.objects.all()
	permission_classes = [IsAdminUser]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	@swagger_auto_schema(tags=["Admin"])
	def get(self, request, *args, **kwargs):
		"""
		List all brands on the platform 
		"""
		print(request.user)
		return self.list(request, *args, **kwargs)

	




