# Generated by Django 2.2.3 on 2019-07-21 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_logs', '0002_auto_20190720_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='file_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
