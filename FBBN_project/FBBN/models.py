from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


# Agnostic
    #User

#Parts (Multiple) - Linked to User

# Linked
    #Build - Multiple Parts, Linked to User
    #Build_Cart - Multiple Parts, Linked to User
    #Part_Likes - User, Part
    #Build Likes - User, Part

# when ready -> 
    # python3 manage.py makemigrations
    # python3 manage.py migrate

# seed data ->
    # Get Seed Data from Django dashboard:  python3 manage.py dumpdata FBBN.part_accessory FBBN.part_bike FBBN.part_rack FBBN.part_seat FBBN.part_storage FBBN.part_trailer FBBN.build FBBN.build_like FBBN.accessory_like FBBN.bike_like FBBN.seat_like FBBN.storage_like FBBN.trailer_like FBBN.rack_like --indent 4 > seed/seed_data_FBBN.json
    # Assumes two users exist on the Django end

# #USER

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     profile_pic_url = models.TextField()
#     is_admin = models.BooleanField()

#     def __str__(self):
#         return self.username

# models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# PARTS

class Part_Accessory(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url_product = models.TextField()
    url_picture = models.TextField()
    other_notes = models.TextField()
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    is_electric_assist = models.BooleanField()
    category = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    frame_materials = models.CharField(max_length=100)
    url_product = models.TextField(blank=True, null=True)
    url_picture = models.TextField(blank=True, null=True)
    other_notes = models.TextField(blank=True, null=True)
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Rack(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    location_on_bike = models.CharField(max_length=100)
    max_weight_lb = models.CharField(max_length=100, blank=True, null=True)
    url_product = models.TextField(blank=True, null=True)
    url_picture = models.TextField(blank=True, null=True)
    other_notes = models.TextField(blank=True, null=True)
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Seat(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mounting_type = models.CharField(max_length=100)
    location_on_bike = models.CharField(max_length=100)
    url_product = models.TextField(blank=True, null=True)
    url_picture = models.TextField(blank=True, null=True)
    other_notes = models.TextField(blank=True, null=True)
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Storage(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mounting_type = models.CharField(max_length=100)
    volume_liters = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    url_product = models.TextField(blank=True, null=True)
    url_picture = models.TextField(blank=True, null=True)
    other_notes = models.TextField(blank=True, null=True)
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Trailer(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    passenger_count = models.IntegerField(validators=[MinValueValidator(0)])
    is_stroller = models.BooleanField(default=False)
    url_product = models.TextField(blank=True, null=True)
    url_picture = models.TextField(blank=True, null=True)
    other_notes = models.TextField(blank=True, null=True)
    added_by_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

# LINKED
class Build(models.Model):
    owner_user = models.ForeignKey(User, on_delete=models.CASCADE)
    build_name = models.CharField(max_length=100)
    build_notes = models.TextField(blank=True, null=True)
    url_build_pic = models.TextField(blank=True, null=True)
    build_bike = models.ForeignKey(Part_Bike, null=True, on_delete=models.SET_NULL)
    build_trailers = models.ManyToManyField(Part_Trailer, blank=True)
    build_seats = models.ManyToManyField(Part_Seat, blank=True)
    build_racks = models.ManyToManyField(Part_Rack, blank=True)
    build_storages = models.ManyToManyField(Part_Storage, blank=True)
    build_accessories = models.ManyToManyField(Part_Accessory, blank=True)

    def __str__(self):
        return self.build_name

class Build_Like(models.Model):
    build = models.ForeignKey(Build, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.build} Like"

class Accessory_Like(models.Model):
    accessory = models.ForeignKey(Part_Accessory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.accessory} Like"

class Bike_Like(models.Model):
    bike = models.ForeignKey(Part_Bike, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bike} Like"

class Rack_Like(models.Model):
    rack = models.ForeignKey(Part_Rack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rack} Like"

class Seat_Like(models.Model):
    seat = models.ForeignKey(Part_Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.seat} Like"

class Storage_Like(models.Model):
    storage = models.ForeignKey(Part_Storage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.storage} Like"

class Trailer_Like(models.Model):
    trailer = models.ForeignKey(Part_Trailer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trailer} Like"