# Generated by Django 2.2.12 on 2020-06-02 05:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLevel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('parent_admin_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.AdminLevel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Lag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('on_time_duration', models.IntegerField(default=1)),
                ('on_time_type', models.CharField(choices=[('minute', 'Minute'), ('hour', 'Hour'), ('day', 'Day')], max_length=10)),
                ('unreported_duration', models.IntegerField(default=1)),
                ('unreported_type', models.CharField(choices=[('minute', 'Minute'), ('hour', 'Hour'), ('day', 'Day')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('shortname', models.CharField(max_length=150, unique=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MeasurementUnit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('shortname', models.CharField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('parent_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.MeasurementUnit')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('admin_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.AdminLevel')),
                ('parent_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('shortname', models.CharField(max_length=150, unique=True)),
                ('quantity', models.PositiveIntegerField()),
                ('base_unit_of_measurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='base_uom_items', to='main.MeasurementUnit')),
                ('item_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='item_type_items', to='main.ItemType')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Program')),
                ('unit_of_measurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uom_items', to='main.MeasurementUnit')),
            ],
        ),
    ]
