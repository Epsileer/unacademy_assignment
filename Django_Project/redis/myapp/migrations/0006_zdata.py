# Generated by Django 3.0.5 on 2020-04-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_data_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
