# Generated by Django 2.2.24 on 2022-08-09 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0085_auto_20220730_0945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsorshippackage',
            options={'ordering': ('-year', 'order')},
        ),
    ]
