# Generated by Django 4.2.4 on 2023-08-23 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_transaction_country_alter_transaction_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='header',
            field=models.TextField(blank=True, null=True),
        ),
    ]