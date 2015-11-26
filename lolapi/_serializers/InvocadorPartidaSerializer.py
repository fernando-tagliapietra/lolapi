from lolapi.models import InvocadorPartida

from rest_framework import serializers


from lolapi.models import Partida
class PartidaSerializer(serializers.ModelSerializer):
    
   class Meta:
        model = Partida
        fields = ('id', 'mapa_id', 'data_partida', 'duracao', 'partida_id', 'modo', 'tipo', 'versao', 'plataforma', 'regiao')

        
class InvocadorPartidaSerializer(serializers.ModelSerializer):

   partida = PartidaSerializer()


   class Meta:
        model = InvocadorPartida
        fields = ('id', 'partida', 'invocador_id', 'campeao_id', 'ultimo_tier', 'participant_id', 'spell', 'spell2', 'time_id', 
                        'assists', 'kills', 'deaths', 'level', 'combat_score', "double_kill", "firstblood_assist", "firstblood_kill",
                        'firsttower_assist', 'firsttower_kill', 'ouro_ganho', 'ouro_gasto','killing_spree', 'maior_critico', 'maior_ks',
                        'maior_multikill', 'danoap_recebido', 'danoap_recebido_champs', 'danoap_feito', 'minions_killed', 'minions_neutro_killed',
                        'minions_neutro_killed_enemy', 'minions_neutro_killed_team', 'pentakill', 'danoad_recebido','danoap_recebido_champs', 'danoad_feito',
                        'quadrakill', 'wards', 'total_dano_recebido', 'total_dano_recebido_champ', 'total_dano_recebido', 'total_dano_recebido_champ',
                        'total_dano_feito', 'total_cura', 'total_tf', 'total_unidades_curadas', 'triplekill', 'dano_verdadeiro_recebido', 'danoap_recebido_champs',
                        'dano_verdadeiro_feito', 'unrealkill', 'pink_wards', 'wards_killed', 'wards_colocadas', 'winner')