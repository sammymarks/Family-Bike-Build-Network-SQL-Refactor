from django.urls import path
from .views import Part_Accessory_List, Part_Accessory_Detail, User_List, User_Detail
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('users/', User_List.as_view(), name='User-list'),
    path('users/<int:pk>', User_Detail.as_view()),    
    path('parts/accessories/', Part_Accessory_List.as_view(), name='part_accessory-list'),
    path('parts/accessories/<int:pk>', Part_Accessory_Detail.as_view(), name='part_accessory-detail'),
]
