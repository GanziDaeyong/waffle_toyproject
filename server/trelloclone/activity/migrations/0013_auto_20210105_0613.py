# Generated by Django 3.1 on 2021-01-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0012_auto_20210105_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_at',
            field=models.DateTimeField(blank=True, default='2021-01-05 06:13:51'),
        ),
    ]