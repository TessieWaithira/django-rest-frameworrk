from django.shortcuts import render
from rest_framework import generics
from .serializers import SnippetsSerializer
from .models import Snippets

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetsSerializer
