# Generated by Django 2.2.1 on 2019-06-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190623_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
