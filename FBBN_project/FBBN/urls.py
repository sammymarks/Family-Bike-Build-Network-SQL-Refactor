from django.urls import path
from .views import Part_Accessory_List, Part_Accessory_Detail
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('accessory/', Part_Accessory_List.as_view(), name='part_accessory-list'),
    path('accessory/<int:pk>', Part_Accessory_Detail.as_view(), name='part_accessory-detail'),
]
