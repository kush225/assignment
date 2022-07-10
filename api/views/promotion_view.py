from api.models.brands import Brand
from api.models.promotions import Promotion
from api.permissions.userPermission import IsBrandUser
from api.serializers.promotion_serializer import PromotionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class PromotionList(generics.ListAPIView):
	"""
	List all promotion of the plan
	"""
	model = Promotion
	serializer_class = PromotionSerializer
	queryset = Promotion.objects.all()
	permission_classes = [IsBrandUser]	

	def get_queryset(self, request): 
		plan_id = self.kwargs['plan_id']
		return self.queryset.filter(plan_id=plan_id)

	@swagger_auto_schema(tags=["Brand"])
	def get(self, request, *args, **kwargs):
		instance = self.get_queryset(request)
		serializer = PromotionSerializer(instance, many=True)
		return Response(serializer.data)

	

class PromotionCreate(generics.CreateAPIView):
	"""
	Add a new promotion in plan
	"""
	model = Promotion
	serializer_class = PromotionSerializer
	queryset = Promotion.objects.all()
	permission_classes = [IsBrandUser]

	@swagger_auto_schema(tags=["Brand"])
	def post(self, request, *args, **kwargs):
		"""
		Add a promotion
		"""
		return self.create(request, *args, **kwargs)


