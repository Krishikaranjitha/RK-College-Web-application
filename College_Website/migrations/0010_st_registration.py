# Generated by Django 5.0.6 on 2024-06-24 18:33

import College_Website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College_Website', '0009_st_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='St_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Fathers_name', models.CharField(blank=True, max_length=20, null=True)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Address', models.TextField(blank=True, max_length=500, null=True)),
                ('Department', models.CharField(choices=[('CSE', 'Computer science and Engineering'), ('EEE', 'Electrical and Electronics Engineering'), ('ECE', 'Electronics and communication Engineering'), ('CE', 'Civil Engineering'), ('ME', 'Mechanical Engineering')], max_length=255)),
                ('Reg_number', models.CharField(max_length=20, unique=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=50)),
                ('Blood_Group', models.CharField(blank=True, choices=[('B+ve', 'B+ve'), ('A+ve', 'A+ve'), ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'), ('O+ve', 'O-ve')], max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=College_Website.models.getFileName)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Tamil', models.IntegerField(default=0)),
                ('English', models.IntegerField(default=0)),
                ('Maths', models.IntegerField(default=0)),
                ('Physics', models.IntegerField(default=0)),
                ('Chemistry', models.IntegerField(default=0)),
                ('Biology', models.IntegerField(default=0)),
                ('Total', models.IntegerField(default=0, editable=False)),
                ('Average', models.FloatField(default=0.0, editable=False)),
            ],
        ),
    ]
