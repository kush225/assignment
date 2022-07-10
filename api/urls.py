
from django.contrib import admin
from django.urls import path, re_path, include
from api.views.brand_view import BrandCreate, BrandList

from api.views.plan_view import PlanList, BrandPlansList, BrandPlansListing
from api.views.promotion_view import PromotionCreate, PromotionList
from api.views.customer_goals_view import CustomerGoalsList
from api.views.customer_user_view import RegisterUserAPIView
from api.views.brand_user_view import BrandRegisterUserAPIView

urlpatterns = [
    path('brand/<str:brand_id>/plans/', PlanList.as_view()),
    path('brand/plans/', BrandPlansListing.as_view()),
    path('promotions/', PromotionCreate.as_view()),
    path('promotions/<int:plan_id>', PromotionList.as_view()),
    path('customer_goals/', CustomerGoalsList.as_view()),
    path('brand/', BrandCreate.as_view()),
    path('brands/', BrandList.as_view()),
    path('plans/', BrandPlansList.as_view()),
    # path("brand/user/details",BrandUserDetailAPI.as_view()),
    path('brand/createuser/',BrandRegisterUserAPIView.as_view()),
    # path("customer/user/details",UserDetailAPI.as_view()),
    path('customer/createuser/',RegisterUserAPIView.as_view()),
    ]
