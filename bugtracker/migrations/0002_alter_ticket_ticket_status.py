# Generated by Django 3.2.6 on 2021-08-31 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_status',
            field=models.CharField(choices=[('New', 'New'), ('Progress', 'In Progress'), ('Done', 'Done'), ('Invalid', 'Invalid')], default='New', max_length=15),
        ),
    ]
