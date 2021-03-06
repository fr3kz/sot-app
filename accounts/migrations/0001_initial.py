# Generated by Django 2.1.4 on 2019-01-22 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lobby', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('thumbnail', models.ImageField(upload_to='media/accounts')),
                ('gold', models.IntegerField()),
                ('solus', models.IntegerField()),
                ('alliance', models.IntegerField()),
                ('reputation', models.IntegerField()),
                ('lobbies', models.ManyToManyField(to='lobby.Queue')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
