# Generated by Django 2.0.8 on 2018-10-13 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebBoard', '0013_profile_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tag',
        ),
    ]
