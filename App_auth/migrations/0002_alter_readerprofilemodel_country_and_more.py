# Generated by Django 4.2.2 on 2023-07-01 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readerprofilemodel',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='researcherprofilemodel',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reviewerprofilemodel',
            name='country',
            field=models.CharField(max_length=255),
        ),
    ]
