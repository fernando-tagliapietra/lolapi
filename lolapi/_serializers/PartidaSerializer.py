from lolapi.models import Partida

from rest_framework import serializers

class PartidaSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = Partida
        fields = ('id', 'mapa_id', 'data', 'duracao', 'partida_id', 'modo', 'tipo', 'versao', 'plataforma', 'regiao')

        
    
