# Generated by Django 5.1.2 on 2024-10-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PressureData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('substance', models.CharField(max_length=20)),
                ('min_pressure', models.FloatField()),
                ('depth_range', models.FloatField()),
                ('pressure_gradient', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]