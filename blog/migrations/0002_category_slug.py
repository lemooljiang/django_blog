# Generated by Django 2.0.7 on 2018-07-03 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]