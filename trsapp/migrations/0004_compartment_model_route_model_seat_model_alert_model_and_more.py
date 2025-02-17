# Generated by Django 5.1.4 on 2025-01-25 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trsapp', '0003_alter_user_model_age_alter_user_model_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compartment_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compartment_name', models.CharField(blank=True, max_length=100, null=True)),
                ('compartment_type', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Route_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(blank=True, max_length=100, null=True)),
                ('destination', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(blank=True, max_length=100, null=True)),
                ('seat_status', models.CharField(blank=True, max_length=100, null=True)),
                ('seat_type', models.CharField(blank=True, max_length=100, null=True)),
                ('COMPARTMENT_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.compartment_model')),
                ('compartment_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.complaint_model')),
            ],
        ),
        migrations.CreateModel(
            name='Alert_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alertmsg', models.CharField(blank=True, max_length=100, null=True)),
                ('extrainfo', models.CharField(blank=True, max_length=100, null=True)),
                ('USER_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.user_model')),
                ('COMPARTMENT_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.compartment_model')),
                ('seat_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.seat_model')),
            ],
        ),
        migrations.CreateModel(
            name='Station_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ROUTE_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.route_model')),
            ],
        ),
        migrations.CreateModel(
            name='Train_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_number', models.CharField(blank=True, max_length=100, null=True)),
                ('train_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ROUTE_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.route_model')),
            ],
        ),
        migrations.CreateModel(
            name='Status_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival', models.CharField(blank=True, max_length=100, null=True)),
                ('departure', models.CharField(blank=True, max_length=100, null=True)),
                ('STATION_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.station_model')),
                ('TRAIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.train_model')),
            ],
        ),
        migrations.AddField(
            model_name='seat_model',
            name='TRAIN_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.train_model'),
        ),
        migrations.AddField(
            model_name='compartment_model',
            name='TRAIN_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.train_model'),
        ),
        migrations.CreateModel(
            name='Booking_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SOURCE', models.CharField(blank=True, max_length=100, null=True)),
                ('DESTINATION', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('USER_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.user_model')),
                ('COMPARTMENT_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.compartment_model')),
                ('SEAT_NO', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.seat_model')),
                ('TRAIN_ID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trsapp.train_model')),
            ],
        ),
    ]
