from lolapi.models import InvocadorTalento

from rest_framework import serializers

class InvocadorSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = InvocadorTalento
        fields = ('id', 'invocador_partida', 'talento_id')

        
    
