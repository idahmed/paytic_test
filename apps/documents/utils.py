from django.core.exceptions import ValidationError


def validate_file_size(value):
    # Limit the file size to 10 MB (10 * 1024 * 1024 bytes)
    max_size = 10 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("File size must be no more than 10 MB.")
