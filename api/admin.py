from django.contrib import admin
from api.models import Brand, Plan, Promotion, CustomerGoal,User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Brand)
admin.site.register(Plan)
admin.site.register(Promotion)
admin.site.register(CustomerGoal)
