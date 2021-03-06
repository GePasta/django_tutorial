# Generated by Django 3.1.2 on 2020-10-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201025_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='mass',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='sex',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
