from lolapi.models import Item

from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = Item
        fields = ('id', 'item_id', 'nome', 'descricao')