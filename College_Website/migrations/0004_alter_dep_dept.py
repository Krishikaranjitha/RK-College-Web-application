# Generated by Django 5.0.6 on 2024-06-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College_Website', '0003_remove_st_results_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dep',
            name='Dept',
            field=models.CharField(max_length=255),
        ),
    ]