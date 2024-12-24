# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Company(models.Model):

    #__Company_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    tax_id = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Company_FIELDS__END

    class Meta:
        verbose_name        = _("Company")
        verbose_name_plural = _("Company")


class Employee(models.Model):

    #__Employee_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    personal_id = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    role = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    shift = models.CharField(max_length=255, null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Employeetype(models.Model):

    #__Employeetype_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)

    #__Employeetype_FIELDS__END

    class Meta:
        verbose_name        = _("Employeetype")
        verbose_name_plural = _("Employeetype")


class Vehicle(models.Model):

    #__Vehicle_FIELDS__
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_available = models.BooleanField()

    #__Vehicle_FIELDS__END

    class Meta:
        verbose_name        = _("Vehicle")
        verbose_name_plural = _("Vehicle")


class Vehicletype(models.Model):

    #__Vehicletype_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Vehicletype_FIELDS__END

    class Meta:
        verbose_name        = _("Vehicletype")
        verbose_name_plural = _("Vehicletype")


class Shift(models.Model):

    #__Shift_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)
    start_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Shift_FIELDS__END

    class Meta:
        verbose_name        = _("Shift")
        verbose_name_plural = _("Shift")


class Service(models.Model):

    #__Service_FIELDS__
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Service_FIELDS__END

    class Meta:
        verbose_name        = _("Service")
        verbose_name_plural = _("Service")


class Team(models.Model):

    #__Team_FIELDS__
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    vehicles = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    #__Team_FIELDS__END

    class Meta:
        verbose_name        = _("Team")
        verbose_name_plural = _("Team")


class Routing(models.Model):

    #__Routing_FIELDS__
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_datetime = models.DateTimeField(blank=True, null=True, default=timezone.now)
    distance_km = models.IntegerField(null=True, blank=True)

    #__Routing_FIELDS__END

    class Meta:
        verbose_name        = _("Routing")
        verbose_name_plural = _("Routing")


class Cost(models.Model):

    #__Cost_FIELDS__
    description = models.CharField(max_length=255, null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    #__Cost_FIELDS__END

    class Meta:
        verbose_name        = _("Cost")
        verbose_name_plural = _("Cost")


class Workprojection(models.Model):

    #__Workprojection_FIELDS__
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    estimated_cost = models.IntegerField(null=True, blank=True)

    #__Workprojection_FIELDS__END

    class Meta:
        verbose_name        = _("Workprojection")
        verbose_name_plural = _("Workprojection")



#__MODELS__END
