from api.models.brands import Brand
from api.models.customer_goals import CustomerGoal
from api.models.promotions import Promotion
from api.permissions.userPermission import IsBrandUser, IsCustomer
from api.serializers.customer_goals_serializer import CustomerGoalCreateSerializer, CustomerGoalSerializer
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import F
from rest_framework.response import Response


class CustomerGoalsList(generics.ListAPIView, generics.CreateAPIView):
		"""
		List all customerGoals on the platform 
		"""
		model = CustomerGoal
		serializer_class = CustomerGoalSerializer
		queryset = CustomerGoal.objects.all()
		permission_classes = []

		def get_permissions(self):
				# Add default permission from post method(Create method)
				if self.request.method == 'GET':
					return (IsBrandUser(),)
				return (IsCustomer(),)

		def get_serializer_class(self, *args, **kwargs):
			if self.request.method == 'POST':
				return CustomerGoalCreateSerializer
			return CustomerGoalSerializer

		def perform_create(self, serializer):
			data = serializer.validated_data
			plan =  data['plan']
			promotion = Promotion.objects.filter(plan_id = plan.pk, is_active=True)
			promotion.update(users_enrolled=F('users_enrolled')+1)
			promotion = promotion.last()
			depositedAmount = data['selectedAmount']/ data['selectedTenure'] 
			benefitPercentage = promotion.benefitPercentage 
			serializer.save(
				user=self.request.user, 
				depositedAmount=depositedAmount, 
				promotion=promotion,
				benefitPercentage=benefitPercentage,
				benefitType= plan.benefitType,
				brand_id=plan.brand_id )

		def get_queryset(self, request): 
			brand = Brand.objects.filter(user_id=request.user.id)
			return self.queryset.filter(brand_id__in=brand.all())

		@swagger_auto_schema(tags=["Brand"])
		def get(self, request, *args, **kwargs):
				instance = self.get_queryset(request)
				serializer = CustomerGoalSerializer(instance, many=True)
				return Response(serializer.data)

		@swagger_auto_schema(tags=["Customer"])
		def post(self, request, *args, **kwargs):
				"""
				Add a goal
				"""
				return self.create(request, *args, **kwargs)

