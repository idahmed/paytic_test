import json
from apps.documents.utils.db_client import connect
from rest_framework import viewsets
from rest_framework.response import Response
from apps.documents.models import Document
from .serializers import DocumentSerializer, TransactionSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response(instance.file.read())

        # <<<<<here if you need file content in db>>>>>

        # if transactions := instance.transactions.all():
        #     data = TransactionSerializer(transactions, many=True).data

        # else:
        #     db = connect()
        #     data = [
        #         json.dumps(item, default=str)
        #         for item in db.find({"document": instance.id})
        #     ]
        # return Response(data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            content = serializer.validated_data["new_content"]

            with instance.file.open("wb") as f:
                for chunk in content:
                    f.write(chunk.encode())

            return Response(serializer.data)

        return Response(serializer.errors, status=400)
