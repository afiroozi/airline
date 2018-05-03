# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Customer(models.Model):
    cus_code = models.IntegerField(primary_key=True)
    cus_lname = models.CharField(max_length=15, blank=True, null=True)
    cus_fname = models.CharField(max_length=15, blank=True, null=True)
    cus_initial = models.CharField(max_length=1, blank=True, null=True)
    cus_areacode = models.CharField(max_length=3, blank=True, null=True)
    cus_phone = models.CharField(max_length=8, blank=True, null=True)
    cus_balance = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

    def __str__(self):
        return self.cus_fname + ' ' + self.cus_lname




class Aircraft(models.Model):
    ac_number = models.CharField(primary_key=True, max_length=5)
    mod_code = models.ForeignKey('Model', models.DO_NOTHING, db_column='mod_code', blank=True, null=True)
    ac_ttaf = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    ac_ttel = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    ac_tter = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aircraft'

    def __str__(self):
        return self.ac_number


class Charter(models.Model):
    char_trip = models.IntegerField(primary_key=True)
    char_date = models.DateField(blank=True, null=True)
    ac_number = models.ForeignKey(Aircraft, models.DO_NOTHING, db_column='ac_number', blank=True, null=True)
    char_destination = models.CharField(max_length=3, blank=True, null=True)
    char_distance = models.IntegerField(blank=True, null=True)
    char_hours_flown = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    char_hours_wait = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    char_fuel_gallons = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    char_oil_qts = models.IntegerField(blank=True, null=True)
    cus_code = models.ForeignKey(Customer, models.DO_NOTHING, db_column='cus_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charter'

    def __str__(self):
        return self.char_trip


class Crew(models.Model):
    char_trip = models.ForeignKey(Charter, models.DO_NOTHING, db_column='char_trip')
    emp_num = models.ForeignKey('Employee', models.DO_NOTHING, db_column='emp_num')
    crew_job = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crew'
        unique_together = (('char_trip', 'emp_num'),)


class Earnedrating(models.Model):
    emp_num = models.ForeignKey('Employee', models.DO_NOTHING, db_column='emp_num')
    rtg_code = models.ForeignKey('Rating', models.DO_NOTHING, db_column='rtg_code')
    earnrtg_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'earnedrating'
        unique_together = (('emp_num', 'rtg_code'),)


class Employee(models.Model):
    emp_num = models.IntegerField(primary_key=True)
    emp_title = models.CharField(max_length=4, blank=True, null=True)
    emp_lname = models.CharField(max_length=15, blank=True, null=True)
    emp_fname = models.CharField(max_length=15, blank=True, null=True)
    emp_initial = models.CharField(max_length=1, blank=True, null=True)
    emp_dob = models.DateField(blank=True, null=True)
    emp_hire_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

    def __str__(self):
        return self.emp_title + ' ' + self.emp_lname


class Model(models.Model):
    mod_code = models.CharField(primary_key=True, max_length=10)
    manufacturer = models.CharField(max_length=15, blank=True, null=True)
    mod_name = models.CharField(max_length=20, blank=True, null=True)
    mod_seats = models.IntegerField(blank=True, null=True)
    mod_chg_mile = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'


class Pilot(models.Model):
    emp_num = models.ForeignKey(Employee, models.DO_NOTHING, db_column='emp_num')
    pil_license = models.CharField(max_length=25, blank=True, null=True)
    pil_ratings = models.CharField(max_length=30, blank=True, null=True)
    pil_med_type = models.CharField(max_length=1, blank=True, null=True)
    pil_med_date = models.DateField(blank=True, null=True)
    pil_pt135_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pilot'


class Rating(models.Model):
    rtg_code = models.CharField(primary_key=True, max_length=5)
    rtg_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'
