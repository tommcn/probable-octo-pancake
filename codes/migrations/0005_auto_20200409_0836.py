# Generated by Django 3.0.4 on 2020-04-09 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0004_auto_20200402_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='code',
            field=models.BigIntegerField(),
        ),
    ]
