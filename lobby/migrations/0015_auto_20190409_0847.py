# Generated by Django 2.1.7 on 2019-04-09 06:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0014_auto_20190409_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='invitator',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
