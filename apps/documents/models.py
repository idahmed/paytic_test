from django.db import models
from django.core.validators import FileExtensionValidator
from apps.documents.utils import validate_file_size


class Document(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    file = models.FileField(
        upload_to="documents/%Y/%m/%d",
        validators=[
            # only accept csv and txt
            FileExtensionValidator(allowed_extensions=["csv", "txt"]),
            # limit file size in 10mib
            validate_file_size,
        ],
        null=False,
        blank=False,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Transaction(models.Model):
    document = models.ForeignKey(
        Document,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="transactions",
    )
    amount = models.IntegerField(null=False, blank=False)
    merchant = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    currency = models.CharField(max_length=255, null=False, blank=False)
    trans_id = models.IntegerField(null=False, blank=False)
