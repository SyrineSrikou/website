# Generated by Django 3.1.1 on 2020-09-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_auto_20200902_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='qualifications',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='responsibility',
            field=models.TextField(blank=True),
        ),
    ]
