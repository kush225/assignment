from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.customer_user_serializer import UserRegisterSerializer
# from django.contrib.auth.models import User
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from api.models.user import TYPE_CHOICES

# class UserDetailAPI(APIView):
# 	@swagger_auto_schema(tags=["Customer"])
# 	def get(self,request,*args,**kwargs):
# 		user = User.objects.get(id=request.user.id)
# 		serializer = UserSerializer(user)
# 		return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
	permission_classes = (AllowAny,)
	serializer_class = UserRegisterSerializer

	@swagger_auto_schema(tags=["Customer"])
	def post(self, request, format=None):
		serializer = UserRegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)