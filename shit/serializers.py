from .models import Note
from rest_framework.serializers import ModelSerializer



class Noteserializer(ModelSerializer):

    class Meta:
        model = Note
        fields = ['note', 'date_at', 'idf']