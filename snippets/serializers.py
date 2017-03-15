from rest_framework import serializers
from .models import Snippets

class SnippetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')