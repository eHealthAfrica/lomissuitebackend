from django.contrib import admin
from main.models import *

# Register your models here.
@admin.register(AdminLevel)
class AdminLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_admin_level',)


@admin.register(MeasurementUnit)
class MeasurementUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'parent_unit', 'is_active',)


@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(CustomerType)
class CustomerTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'start_date', 'end_date',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'item_type', 'program', 'quantity', 'unit_of_measurement', 'base_unit_of_measurement',)


@admin.register(Lag)
class LagAdmin(admin.ModelAdmin):
    list_display = ('name', 'on_time_duration', 'on_time_type', 'unreported_duration', 'unreported_type',)
