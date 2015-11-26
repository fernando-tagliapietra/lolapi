from lolapi.models import Invocador

from rest_framework import serializers

class InvocadorSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = Invocador
        fields = ('id', 'api_id', 'nome', 'tier', 'divisao', 'icone', 'nivel', 'regiao', 'data_atualizacao', 
                        'liga_nome', 'pdl', 'wins', 'loses', 'series')

        
    
