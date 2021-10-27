from django.db import models

# Create your models here.
class Volunteer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    avail_mon = models.BooleanField(default=False)
    avail_tues = models.BooleanField(default=False)
    avail_wed = models.BooleanField(default=False)
    avail_thurs = models.BooleanField(default=False)
    avail_fri = models.BooleanField(default=False)