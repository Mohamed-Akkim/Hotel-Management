# Generated by Django 4.2.5 on 2024-01-18 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesentryform',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expensesentryform',
            name='particular',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
