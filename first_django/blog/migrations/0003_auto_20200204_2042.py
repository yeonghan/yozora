# Generated by Django 3.0.2 on 2020-02-04 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200128_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Post',
            new_name='post',
        ),
    ]
