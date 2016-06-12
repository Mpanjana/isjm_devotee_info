from __future__ import unicode_literals
from django.db import models


# Create your models here.
class DevoteesMaterialInfo(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, null=True)
    marital_status = models.CharField(max_length=200, null=True)
    date_of_birth = models.CharField(max_length=200,default=None, null=True)
    time_of_birth = models.CharField(max_length=200, null=True)
    place_of_birth = models.CharField(max_length=200, null=True)
    current_address = models.TextField(null=True)
    permanent_address = models.TextField(null=True)
    email = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=50)
    Profession = models.TextField(null=True)


class DevoteesSpiritualInfo(models.Model):
    devotee = models.ForeignKey(DevoteesMaterialInfo)
    spiritual_name = models.CharField(max_length=200, null=True)
    diksha_guru = models.CharField(max_length=200, null=True)
    diksha_date = models.DateTimeField(default=None, null=True)
    diksha_place = models.CharField(max_length=200, null=True)
    brahman = models.BooleanField(default=0)
    shiksha_level = models.CharField(max_length=100, null=True)
    chanting_rounds = models.IntegerField(default=0)
    courses = models.CharField(max_length=100, null=True)
    shiksha_guru = models.CharField(max_length=200, null=True)
    life_member = models.CharField(max_length=50, null=True)
    donor_number = models.CharField(max_length=50, null=True)


class DevoteesServiceInfo(models.Model):
    devotee = models.ForeignKey(DevoteesMaterialInfo)
    preaching = models.CharField(max_length=100, null=True)
    services = models.CharField(max_length=100, null=True)
    leader = models.TextField(null=True)


class DevoteesSpouseInfo(models.Model):
    devotee = models.ForeignKey(DevoteesMaterialInfo)
    spiritual_info = models.ForeignKey(DevoteesSpiritualInfo,default=None, null=True)
    service_info = models.ForeignKey(DevoteesServiceInfo,default=None, null=True)
    name = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateTimeField(default=None, null=True)
    time_of_birth = models.CharField(max_length=200, null=True)
    place_of_birth = models.CharField(max_length=200, null=True)
    Profession = models.TextField(null=True)


class DevotessChildrenInfo(models.Model):
    devotee = models.ForeignKey(DevoteesMaterialInfo)
    spiritual_info = models.ForeignKey(DevoteesSpiritualInfo,default=None, null=True)
    service_info = models.ForeignKey(DevoteesServiceInfo,default=None, null=True)
    name = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=200, null=True)
    marital_status = models.CharField(max_length=200, null=True)
    date_of_birth = models.DateTimeField(default=None, null=True)
    time_of_birth = models.CharField(max_length=200, null=True)
    place_of_birth = models.CharField(max_length=200, null=True)
    Profession = models.TextField(null=True)


class DevoteeParentInfo(models.Model):
    devotee = models.ForeignKey(DevoteesMaterialInfo)
    father_name = models.CharField(max_length=200, null=True)
    mother_name = models.CharField(max_length=200, null=True)
    father_spiritual_info = models.ForeignKey(DevoteesSpiritualInfo,default=None, null=True,related_name='father_spiritual_info')
    mother_spiritual_info = models.ForeignKey(DevoteesSpiritualInfo,default=None, null=True,related_name='mother_spiritual_info')
    father_service_info = models.ForeignKey(DevoteesServiceInfo,default=None, null=True,related_name='father_service_info')
    mother_service_info = models.ForeignKey(DevoteesServiceInfo,default=None, null=True,related_name='mother_service_info')