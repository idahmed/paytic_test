# Generated by Django 4.2.4 on 2023-08-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_rename_path_document_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='country',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='currency',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='merchant',
            field=models.IntegerField(),
        ),
    ]
