# Generated by Django 2.2.8 on 2020-02-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providers',
            name='Image',
            field=models.ImageField(default='', upload_to='providers/images'),
        ),
    ]
