# Generated by Django 2.0.2 on 2018-02-24 15:03

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_auto_20180224_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='favourite',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
