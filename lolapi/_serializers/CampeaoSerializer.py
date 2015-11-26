from lolapi.models import Campeao

from rest_framework import serializers

class CampeaoSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = Campeao
        fields = ('id', 'campeao_id', 'nome', 'lane')

        
    
