# Generated by Django 2.1.7 on 2019-08-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190429_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='alliance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='solus',
            field=models.IntegerField(default=0),
        ),
    ]
