# Generated by Django 2.1.7 on 2019-03-16 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0009_queue_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queue',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
