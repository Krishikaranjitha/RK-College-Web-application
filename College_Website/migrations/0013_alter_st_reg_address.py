# Generated by Django 5.0.6 on 2024-07-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College_Website', '0012_alter_st_registration_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='st_reg',
            name='Address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
