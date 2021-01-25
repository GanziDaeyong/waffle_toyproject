# Generated by Django 3.1.3 on 2020-12-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_auto_20201225_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='key',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='created_at',
            field=models.DateTimeField(blank=True, default='2020-12-31 10:32:16'),
        ),
        migrations.AlterField(
            model_name='card',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]