# Generated by Django 2.0.8 on 2018-10-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebBoard', '0008_auto_20181005_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
