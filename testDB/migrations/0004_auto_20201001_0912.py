# Generated by Django 3.1.1 on 2020-10-01 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testDB', '0003_auto_20201001_0601'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestModel',
            new_name='SampleModel',
        ),
    ]