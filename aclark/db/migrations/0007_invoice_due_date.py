# Generated by Django 2.0.1 on 2018-02-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_auto_20180207_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(blank=True, null=True, verbose_name='Due'),
        ),
    ]
