# Generated by Django 2.2.3 on 2019-07-21 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_logs', '0004_alldata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alldata',
            name='user',
        ),
    ]
