from django.contrib import admin
from .models import Part_Accessory, Part_Bike, Part_Rack, Part_Seat, Part_Storage, Part_Trailer, Build, Build_Likes, Accessory_Likes, Bike_Likes, Rack_Likes, Seat_Likes, Storage_Likes, Trailer_Likes

# Register your models here.
admin.site.register(Part_Accessory)
admin.site.register(Part_Bike)
admin.site.register(Part_Rack)
admin.site.register(Part_Seat)
admin.site.register(Part_Storage)
admin.site.register(Part_Trailer)
admin.site.register(Build)
admin.site.register(Build_Likes)
admin.site.register(Accessory_Likes)
admin.site.register(Bike_Likes)
admin.site.register(Seat_Likes)
admin.site.register(Storage_Likes)
admin.site.register(Trailer_Likes)
admin.site.register(Rack_Likes)
