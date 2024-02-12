from django.shortcuts import render
from rest_framework import generics
from .models import Part_Accessory, Part_Bike, Part_Rack, Part_Seat, Part_Storage, Part_Trailer, Build, Build_Like, Accessory_Like, Bike_Like, Rack_Like, Seat_Like, Storage_Like, Trailer_Like
from .serializers import Part_Accessory_Serializer

# Create your views here.
class Part_Accessory_List(generics.ListCreateAPIView):
    queryset = Part_Accessory.objects.all()
    serializer_class = Part_Accessory_Serializer

class Part_Accessory_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Part_Accessory.objects.all()
    serializer_class = Part_Accessory_Serializer
