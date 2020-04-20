# Generated by Django 3.0.5 on 2020-04-19 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('ttl', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
