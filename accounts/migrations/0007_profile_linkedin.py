# Generated by Django 2.2.1 on 2019-06-23 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.URLField(null=True),
        ),
    ]
