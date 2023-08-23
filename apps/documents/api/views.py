from rest_framework import viewsets
from apps.documents.models import Document
from .serializers import DocumentSerializer
from rest_framework.permissions import AllowAny


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
