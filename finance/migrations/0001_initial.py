# Generated by Django 2.2.14 on 2022-01-31 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citoyen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cin', models.CharField(max_length=8, unique=True)),
                ('amende', models.CharField(max_length=100)),
                ('pinalité', models.CharField(max_length=100)),
            ],
        ),
    ]
