# Generated by Django 5.0.6 on 2024-06-24 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('College_Website', '0006_rename_dept_dep_deptt_alter_st_results_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Dep',
        ),
    ]
