from rest_framework import serializers
from apps.documents.models import Document, Transaction


class DocumentSerializer(serializers.ModelSerializer):
    new_content = serializers.CharField(required=False)

    class Meta:
        model = Document
        fields = ("id", "name", "file", "uploaded_at", "new_content", "header")
        extra_kwargs = {
            "new_content": {"write_only": True},
            "name": {"required": False},
            "file": {"required": False},
        }

    def validate(self, validated_data):
        if self.context["view"].action == "update":
            header = validated_data["new_content"].strip().split("\r\n")[0]
            if header != self.instance.header:
                raise serializers.ValidationError("Headers are not changeable")

        if self.context["view"].action == "create":
            if not "file" and "name" in validated_data:
                raise serializers.ValidationError("File or file name is missing")

        return validated_data


class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = (
            "amount",
            "merchant",
            "country",
            "city",
            "currency",
            "trans_id",
        )
