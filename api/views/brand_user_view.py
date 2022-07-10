from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.brand_user_serializer import BrandRegisterSerializer
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from api.models.user import TYPE_CHOICES

# class BrandUserDetailAPI(APIView):
# 	@swagger_auto_schema(tags=["Brand"])
# 	def get(self,request,*args,**kwargs):
# 		user = User.objects.get(id=request.user.id)
# 		serializer = UserSerializer(user)
# 		return Response(serializer.data)


class BrandRegisterUserAPIView(generics.CreateAPIView):
	permission_classes = (AllowAny,)
	serializer_class = BrandRegisterSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

	@swagger_auto_schema(tags=["Brand"])
	def post(self, request, format=None):
		serializer = BrandRegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)