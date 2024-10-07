# Generated by Django 5.0.6 on 2024-07-17 08:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_passwordreset'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnm', models.CharField(max_length=15)),
                ('cat', models.CharField(max_length=15)),
                ('lang', models.CharField(max_length=15)),
                ('publ', models.CharField(max_length=25)),
                ('isbn', models.IntegerField(max_length=15)),
                ('pr', models.FloatField(max_length=15)),
                ('qty', models.IntegerField()),
                ('img', models.ImageField(upload_to='p_images')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]