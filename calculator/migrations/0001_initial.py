# Generated by Django 3.0.1 on 2020-02-24 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField()),
                ('Y', models.FloatField()),
                ('Result', models.FloatField()),
            ],
        ),
    ]