# Generated by Django 3.1 on 2021-01-05 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0014_auto_20210104_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(blank=True, default='2021-01-05 02:46:07'),
        ),
    ]