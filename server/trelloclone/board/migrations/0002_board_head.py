# Generated by Django 3.1.3 on 2020-12-24 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='board_head', to='list.list'),
        ),
    ]