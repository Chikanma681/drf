# Generated by Django 4.1.4 on 2023-01-02 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0006_menuitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
