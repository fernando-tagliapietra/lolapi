from lolapi.models import Usuario

from rest_framework import serializers

class UsuarioInfoSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = Usuario
        fields = ( 'id', 'nome', 'email',  'conta_twitch', 'conta_facebook', 'conta_twitter', 'dias_jogo', 'horarios_jogo', 'invocadores')
        
    
