# Generated by Django 2.0.8 on 2018-10-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebBoard', '0011_auto_20181005_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, default='Nothing', max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hobbies',
            field=models.CharField(blank=True, default='Nothing', max_length=1000),
        ),
    ]
