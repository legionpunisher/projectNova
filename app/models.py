from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name
class Hood(models.Model):
    hood_photo = models.ImageField(upload_to='hoods/')
    hood_name = models.CharField(max_length=100, null=True)
    occupants_count = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(Location, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
