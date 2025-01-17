# Generated by Django 5.0.6 on 2024-06-24 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('College_Website', '0005_alter_dep_dept'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dep',
            old_name='Dept',
            new_name='Deptt',
        ),
        migrations.AlterField(
            model_name='st_results',
            name='Department',
            field=models.CharField(choices=[('CSE', 'Computer science and Engineering'), ('EEE', 'Electrical and Engineering'), ('ECE', 'Electronics and communication Engineering'), ('CE', 'Civil Engineering'), ('ME', 'Mechanical Engineering')], max_length=255),
        ),
    ]
