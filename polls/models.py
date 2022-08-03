from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDERS = (
        ('M', 'مرد'),
        ('F', 'زن'),
        ('U', 'هیچکدام')
    )
    gender = models.CharField(max_length=20, choices=GENDERS)
    biography = models.CharField(max_length=200)


class Course(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=20)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    WEEKDAYS = (
        ('شنبه','شنبه'),
        ('یکشنبه','یکشنبه'),
        ('دوشنبه','دوشنبه'),
        ('سه شنبه','سه شنبه'),
        ('چهارشنبه','چهارشنبه')
    )
    first_day = models.CharField(max_length=10, choices=WEEKDAYS, null=False, blank=False)
    second_day = models.CharField(max_length=10, null=True, blank=True, choices=WEEKDAYS)

    def __str__(self):
        return self.name




