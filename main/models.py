from django.db import models
from django.utils.text import slugify

# Create your models here.
class AdminLevel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    parent_admin_level = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class MeasurementUnit(models.Model):
    name = models.CharField(max_length=150, unique=True)
    shortname = models.CharField(max_length=150, unique=True)
    parent_unit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class TypeBaseModel(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class FacilityType(TypeBaseModel):
    pass


class ItemType(TypeBaseModel):
    pass


class TaskType(TypeBaseModel):
    pass


class CustomerType(TypeBaseModel):
    pass


class Location(models.Model):
    name = models.CharField(max_length=150)
    parent_location = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    admin_level = models.ForeignKey(AdminLevel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=150, unique=True)
    shortname = models.CharField(max_length=150, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=150, unique=True)
    shortname = models.CharField(max_length=150, unique=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True, related_name='item_type_items')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Note: Do we really need the two below, maybe one will suffice
    unit_of_measurement = models.ForeignKey(MeasurementUnit, on_delete=models.SET_NULL, null=True, related_name='uom_items')
    base_unit_of_measurement = models.ForeignKey(MeasurementUnit, on_delete=models.SET_NULL, null=True, related_name='base_uom_items')

    def __str__(self):
        return self.name



class Lag(models.Model):
    LAG_TIME_TYPE_CHOICES = [
        ('minute', 'Minute'),
        ('hour', 'Hour'),
        ('day', 'Day'),
    ]
    name = models.CharField(max_length=150, unique=True)
    on_time_duration = models.IntegerField(default=1)
    on_time_type = models.CharField(max_length=10, choices=LAG_TIME_TYPE_CHOICES)
    unreported_duration = models.IntegerField(default=1)
    unreported_type = models.CharField(max_length=10, choices=LAG_TIME_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
