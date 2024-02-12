from django.contrib import admin
from .models import Part_Accessory, Part_Bike, Part_Rack, Part_Seat, Part_Storage, Part_Trailer, Build, Build_Like, Accessory_Like, Bike_Like, Rack_Like, Seat_Like, Storage_Like, Trailer_Like

# Register your models here.
admin.site.register(Part_Accessory)
admin.site.register(Part_Bike)
admin.site.register(Part_Rack)
admin.site.register(Part_Seat)
admin.site.register(Part_Storage)
admin.site.register(Part_Trailer)
admin.site.register(Build)
admin.site.register(Build_Like)
admin.site.register(Accessory_Like)
admin.site.register(Bike_Like)
admin.site.register(Seat_Like)
admin.site.register(Storage_Like)
admin.site.register(Trailer_Like)
admin.site.register(Rack_Like)
