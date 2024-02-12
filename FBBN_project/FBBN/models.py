from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
# class Artist(models.Model):
#     name = models.CharField(max_length=100)
#     nationality = models.CharField(max_length=100)
#     photo_url = models.TextField()

#     def __str__(self):
#         return self.name


# Agnostic
    #User

# Linked
    #Parts (Multiple) - Linked to User
    #Build - Multiple Parts, Linked to User
    #Build_Cart - Multiple Parts, Linked to User
    #Part_Likes - User, Part
    #Build Likes - User, Part


#USER

class User(models.Model):
    username = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_pic_url = models.TextField()
    is_admin = models.BooleanField()

    def __str__(self):
        return self.username

# PARTS

class Part_Accessory(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url_product = models.TextField()
    url_picture = models.TextField()
    other_notes = models.TextField()
    added_by_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    is_electric_assist = models.BooleanField()
    category = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url_product = models.TextField()
    url_picture = models.TextField()
    other_notes = models.TextField()
    added_by_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Rack(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    location_on_bike = models.CharField(max_length=100)
    max_weight_lb = models.CharField(max_length=100)
    url_product = models.TextField()
    url_picture = models.TextField()
    other_notes = models.TextField()
    added_by_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Seat(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mounting_type = models.CharField(max_length=100)
    location_on_bike = models.CharField(max_length=100)
    url_product = models.TextField()
    url_picture = models.TextField()
    other_notes = models.TextField()
    added_by_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Storage(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    mounting_type = models.CharField(max_length=100)
    volume_liters = models.IntegerField(validators=[MinValueValidator(0)])
    url_product = models.TextField()
    url_picture = models.TextField()
    other_notes = models.TextField()
    added_by_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.brand} {self.model}"

class Part_Trailer(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    passenger_count = models.IntegerField(validators=[MinValueValidator(0)])
    url_product = models.TextField()
    url_picture = models.TextField()
    other_notes = models.TextField()
    added_by_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.brand} {self.model}"

# LINKED
class Build(models.Model):
    owner_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    build_name = models.CharField(max_length=100)
    build_notes = models.TextField()
    url_build_pic = models.TextField()
    build_bike = models.ForeignKey(Part_Bike, null=True, on_delete=models.SET_NULL)
    build_trailers = models.ManyToManyField(Part_Trailer)
    build_seats = models.ManyToManyField(Part_Seat)
    build_racks = models.ManyToManyField(Part_Rack)
    build_storages = models.ManyToManyField(Part_Storage)
    build_accessories = models.ManyToManyField(Part_Accessory)

    def __str__(self):
        return self.build_name

class Build_Likes(models.Model):
    build = models.ForeignKey(Build, null=True, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.build} Likes"

class Accessory_Likes(models.Model):
    accessory = models.ForeignKey(Part_Accessory, null=True, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.accessory} Likes"

class Bike_Likes(models.Model):
    bike = models.ForeignKey(Part_Bike, null=True, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.bike} Likes"

class Rack_Likes(models.Model):
    rack = models.ForeignKey(Part_Rack, null=True, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.rack} Likes"

class Seat_Likes(models.Model):
    seat = models.ForeignKey(Part_Seat, null=True, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.seat} Likes"

class Storage_Likes(models.Model):
    storage = models.ForeignKey(Part_Storage, null=True, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.storage} Likes"

class Trailer_Likes(models.Model):
    trailer = models.ForeignKey(Part_Trailer, null=True, on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.trailer} Likes"