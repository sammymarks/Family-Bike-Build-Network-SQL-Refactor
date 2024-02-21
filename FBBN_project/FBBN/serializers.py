from rest_framework import serializers
# Import User to directly reference the Django Users
from django.contrib.auth.models import User
from .models import Part_Accessory, Part_Bike, Part_Rack, Part_Seat, Part_Storage, Part_Trailer, Build, Build_Like, Accessory_Like, Bike_Like, Rack_Like, Seat_Like, Storage_Like, Trailer_Like

#Users

class User_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


#PARTS

class Part_Accessory_Serializer(serializers.HyperlinkedModelSerializer):
    accessory = serializers.HyperlinkedRelatedField(
        view_name='part-accessory-detail',
        read_only=True
    )

    # added_by_user = serializers.PrimaryKeyRelatedField(
    #     # source='added_by_user',
    #     queryset=User.objects.all()
    # )
    added_by_user = serializers.StringRelatedField()


    class Meta:
        model = Part_Accessory
        fields = '__all__'