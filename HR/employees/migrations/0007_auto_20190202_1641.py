# Generated by Django 2.1.3 on 2019-02-02 16:41

from django.db import migrations, models
import employees.models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_auto_20190202_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='staff_key',
            field=models.CharField(default='x9b11df64', max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalemployeeprofile',
            name='staff_key',
            field=models.CharField(default='x9b11df64', max_length=100),
        ),
        migrations.AlterField(
            model_name='profileimage',
            name='avatar',
            field=models.ImageField(default='default.png', upload_to=employees.models.upload_path_p),
        ),
    ]
