# Generated by Django 5.0.6 on 2024-06-24 08:51

import College_Website.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College_Website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='St_results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Reg_number', models.CharField(max_length=20, unique=True)),
                ('Tamil', models.IntegerField(default=0)),
                ('English', models.IntegerField(default=0)),
                ('Maths', models.IntegerField(default=0)),
                ('Physics', models.IntegerField(default=0)),
                ('Chemistry', models.IntegerField(default=0)),
                ('Biology', models.IntegerField(default=0)),
                ('Total', models.IntegerField(default=0, editable=False)),
                ('Average', models.FloatField(default=0.0, editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=College_Website.models.getFileName)),
                ('status', models.BooleanField(default=False, help_text='0-Show,1-Hidden')),
                ('Department', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='College_Website.dep')),
            ],
        ),
    ]
