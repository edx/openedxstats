# Generated by Django 1.9.5 on 2016-05-20 20:23
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackdata', '0003_auto_20160427_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagecountbyday',
            name='count',
            field=models.IntegerField(null=True),
        ),
    ]
