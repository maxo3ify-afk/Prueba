# Generated by Django 4.2.6 on 2023-10-14 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Origen', models.CharField(max_length=64)),
                ('Destino', models.CharField(max_length=64)),
                ('Duracion', models.IntegerField()),
            ],
        ),
    ]
