# Generated by Django 4.1.9 on 2023-06-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='productattachment',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]