import csv
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.documents.models import Document, Transaction

from pymongo import MongoClient
from pymongo.server_api import ServerApi


@receiver(post_save, sender=Document, dispatch_uid="file_handler")
def file_handler(sender, instance, created, **kwargs):
    if created:
        file = instance.file.path
        file_type = file.split(".")[-1].lower()

        uri = "mongodb+srv://idahmedyassine:JhX3Do5PLdBrD3Bg@cluster0.7jdctvu.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(uri, server_api=ServerApi("1"))
        db = client["paytic"]
        collection = db["transaction"]

        if file_type == "csv":
            with open(file, "r") as csvfile:
                header = next(csv.reader(csvfile))
                reader = csv.DictReader(csvfile)
                if set(header) == set(
                    [
                        "amount",
                        "merchant",
                        "country",
                        "city",
                        "currency",
                        "trans_id",
                    ]
                ):
                    for row in reader:
                        Transaction.objects.create(
                            document=instance,
                            amount=row["amount"],
                            merchant=row["merchant"],
                            country=row["country"],
                            city=row["city"],
                            currency=row["currency"],
                            trans_id=row["trans_id"],
                        )

                else:
                    collection.insert_many(reader)

        elif file_type == "text":
            with open(file, "r") as txtfile:
                first_row = txtfile.readline().strip()
                if set(first_row.split()) == (
                    "amount",
                    "merchant",
                    "country",
                    "city",
                    "currency",
                    "trans_id",
                ):
                    for row in txtfile:
                        Transaction.objects.create(
                            document=instance,
                            amount=row.split()[0],
                            merchant=row.split()[1],
                            country=row.split()[2],
                            city=row.split()[3],
                            currency=row.split()[4],
                            trans_id=row.split()[5],
                        )
