# Generated by Django 3.1.1 on 2020-09-03 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=50)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
