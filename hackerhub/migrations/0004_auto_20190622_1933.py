# Generated by Django 2.2.1 on 2019-06-22 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerhub', '0003_auto_20190622_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackathon',
            name='description',
            field=models.TextField(blank=True, default='', max_length=800),
        ),
    ]
