# Generated by Django 4.2.4 on 2023-08-23 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_remove_document_file_document_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='path',
            new_name='file',
        ),
    ]
