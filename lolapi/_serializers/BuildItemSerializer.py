from lolapi._serializers.BuildSerializer import BuildSerializer
from lolapi._serializers.ItemSerializer import ItemSerializer

from lolapi.models import BuildItem

from rest_framework import serializers

class BuildItemSerializer(serializers.ModelSerializer):

    build = BuildSerializer()
    item  = ItemSerializer()
    
    class Meta:
        model = BuildItem
        fields = ('id', 'build', 'item')