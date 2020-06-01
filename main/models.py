from django.db import models
from django.utils.text import slugify

# Create your models here.
class AdminLevel(models.Model):
    # TODO: Should we add a slug
    name = models.CharField(max_length=150, unique=True)
    parent_admin_level = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=150, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(AdminLevel, self).save(*args, **kwargs)


class MeasurementUnit(models.Model):
    # TODO: Should we add a slug
    name = models.CharField(max_length=150, unique=True)
    shortname = models.CharField(max_length=150, unique=True)
    parent_unit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.shortname)
        super(MeasurementUnit, self).save(*args, **kwargs)


class TypeBaseModel(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class FacilityType(TypeBaseModel):

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(FacilityType, self).save(*args, **kwargs)


class ItemType(TypeBaseModel):

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ItemType, self).save(*args, **kwargs)


class TaskType(TypeBaseModel):

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(TaskType, self).save(*args, **kwargs)


class CustomerType(TypeBaseModel):

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(CustomerType, self).save(*args, **kwargs)


class Location(models.Model):
    name = models.CharField(max_length=150)
    parent_location = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    admin_level = models.ForeignKey(AdminLevel, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=150, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.shortname)
        super(Location, self).save(*args, **kwargs)


class Program(models.Model):
    name = models.CharField(max_length=150, unique=True)
    shortname = models.CharField(max_length=150, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    slug = models.SlugField(max_length=150, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.shortname)
        super(Program, self).save(*args, **kwargs)


class Item(models.Model):
    name = models.CharField(max_length=150, unique=True)
    shortname = models.CharField(max_length=150, unique=True)
    item_type = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True, related_name='item_type_items')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Note: Do we really need the two below, maybe one will suffice
    unit_of_measurement = models.ForeignKey(MeasurementUnit, on_delete=models.SET_NULL, null=True, related_name='uom_items')
    base_unit_of_measurement = models.ForeignKey(MeasurementUnit, on_delete=models.SET_NULL, null=True, related_name='base_uom_items')
    slug = models.SlugField(max_length=150, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.shortname)
        super(Item, self).save(*args, **kwargs)


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
    slug = models.SlugField(max_length=150, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Lag, self).save(*args, **kwargs)
