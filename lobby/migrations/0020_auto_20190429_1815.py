# Generated by Django 2.1.7 on 2019-04-29 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lobby', '0019_auto_20190420_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='queue',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='query',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='query',
            name='queue',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lobby.Queue'),
        ),
        migrations.AlterField(
            model_name='queue',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='lobby.Category'),
        ),
    ]