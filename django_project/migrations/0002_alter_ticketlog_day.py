# Generated by Django 3.2.13 on 2023-10-26 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketlog',
            name='day',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
