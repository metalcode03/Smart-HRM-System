# Generated by Django 2.1.3 on 2019-02-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_auto_20190225_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='employee_temp_profil',
        ),
        migrations.RemoveField(
            model_name='historicalemployeeprofile',
            name='employee_temp_profil',
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='staff_key',
            field=models.CharField(default='x10e02ffc', max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalemployeeprofile',
            name='staff_key',
            field=models.CharField(default='x10e02ffc', max_length=100),
        ),
    ]
