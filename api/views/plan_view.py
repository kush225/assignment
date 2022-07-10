from api.models.brands import Brand
from api.models.plans import Plan
from api.permissions.userPermission import IsBrandUser, IsCustomer
from api.serializers.plan_serializer import PlanSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class PlanList(generics.ListAPIView):
    """
    List all plans on the platform 
    """
    model = Plan
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = [IsCustomer]


    def get_queryset(self, request):
        brand_id = self.kwargs['brand_id']
        return self.queryset.filter(brand_id=brand_id)

    @swagger_auto_schema(tags=["Customer"])
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset(request)
        serializer = PlanSerializer(instance, many=True)
        return Response(serializer.data)

class BrandPlansListing(generics.ListAPIView):
    """
    List all plans of the brand 
    """
    model = Plan
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = [IsBrandUser] 

    def get_queryset(self, request):
        brand = Brand.objects.filter(user_id=request.user.id)
        return self.queryset.filter(brand_id__in=brand.all())

    @swagger_auto_schema(tags=["Brand"])
    def get(self, request, *args, **kwargs):
        instance = self.get_queryset(request)
        serializer = PlanSerializer(instance, many=True)
        return Response(serializer.data)


class BrandPlansList(generics.ListAPIView, generics.CreateAPIView):
    """
    List all plans of the brand 
    """
    model = Plan
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()
    permission_classes = [] 

    def get_permissions(self):
        if self.request.method == 'GET':
            return (IsCustomer(),)
        return (IsBrandUser(),)

    @swagger_auto_schema(tags=["Customer"])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(tags=["Brand"])
    def post(self, request, *args, **kwargs):
        """
        Add a plan
        """
        return self.create(request, *args, **kwargs)
