# Generated by Django 5.0.4 on 2024-05-03 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_event_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
    ]