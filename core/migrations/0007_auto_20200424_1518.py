# Generated by Django 3.0.5 on 2020-04-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200424_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='photo',
            field=models.ImageField(upload_to='media/images'),
        ),
    ]
