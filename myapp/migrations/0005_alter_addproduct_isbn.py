# Generated by Django 5.0.6 on 2024-07-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_addproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='isbn',
            field=models.IntegerField(),
        ),
    ]
