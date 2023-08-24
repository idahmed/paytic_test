import csv
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.documents.models import Document, Transaction

from apps.documents.utils.db_client import connect


@receiver(post_save, sender=Document, dispatch_uid="file_handler")
def file_handler(sender, instance, created, **kwargs):
    if created:
        file = instance.file.path
        collection = connect()

        # here i assumed that the text files have data in CSV format
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            header = list(reader.fieldnames)
            data = []
            for row in reader:
                try:
                    Transaction.objects.create(document=instance, **row)
                except Exception as e:
                    # group all item in list to hit the db once
                    data.append(row | {"document": instance.id})

            if data:
                collection.insert_many(data)

            instance.header = ",".join(header)
            instance.save()
