# Generated by Django 2.1.3 on 2019-02-04 17:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20190203_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='company_url',
            field=models.UUIDField(default=uuid.UUID('c5601fbf-c705-4a7b-b2b0-07f967fc81e7'), editable=False),
        ),
        migrations.AlterField(
            model_name='historicalcompanyprofile',
            name='company_url',
            field=models.UUIDField(default=uuid.UUID('c5601fbf-c705-4a7b-b2b0-07f967fc81e7'), editable=False),
        ),
    ]
