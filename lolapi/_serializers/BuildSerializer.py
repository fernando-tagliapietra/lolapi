from lolapi.models import Build

from rest_framework import serializers

class BuildSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = Build
        fields = ('id', 'descricao' , 'magia1', 'magia2', 'usuario', 'campeao', 'temporada', 'items')
        depth = 1