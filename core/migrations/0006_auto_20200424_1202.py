# Generated by Django 3.0.5 on 2020-04-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200424_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponsojects',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]