# Generated by Django 3.0.7 on 2020-06-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20200617_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortener',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]