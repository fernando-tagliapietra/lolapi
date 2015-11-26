# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Build(models.Model):
    ##id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    descricao = models.CharField(max_length=50, blank=True)
    magia1 = models.CharField(max_length=50, blank=True)
    magia2 = models.CharField(max_length=50, blank=True)
    usuario = models.ForeignKey("Usuario")#models.IntegerField(blank=True, null=True)
    campeao = models.ForeignKey("Campeao")#models.IntegerField(blank=True, null=True)
    temporada = models.IntegerField(blank=True, null=True)
    items = models.ManyToManyField("Item", through='BuildItem')

    class Meta:
        managed = False
        db_table = 'Build'


class BuildItem(models.Model):
    ##id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    build = models.ForeignKey("Build")#models.IntegerField(blank=True, null=True)
    item  = models.ForeignKey("Item")#models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Build_Item'


class Campeao(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    campeao_id = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True)
    lane = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'Campeao'


class Guia(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    usuario = models.ForeignKey("Usuario")#models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True)
    html = models.TextField(blank=True)
    votos_positivos = models.IntegerField(blank=True, null=True)
    votos_negativos = models.IntegerField(blank=True, null=True)
    aprovado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Guia'


class Invocador(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    api_id = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True)
    tier = models.CharField(max_length=50, blank=True)
    divisao = models.IntegerField(blank=True, null=True)
    icone = models.IntegerField(blank=True, null=True)
    nivel = models.IntegerField(blank=True, null=True)
    regiao = models.CharField(max_length=5, blank=True)
    data_atualizacao = models.DateTimeField(auto_now_add=True, blank=True)
    liga_nome = models.CharField(max_length=50, blank=True)
    liga_id = models.IntegerField(blank=True, null=True)
    pdl = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    loses = models.IntegerField(blank=True, null=True)
    series = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'Invocador'


class InvocadorpartidaItem(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    item_id = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'InvocadorPartida_Item'


class InvocadorLiga(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    invocador_nome = models.CharField(max_length=100, blank=True)
    liga_id = models.IntegerField(blank=True, null=True)
    liga_nome = models.CharField(max_length=50, blank=True)
    tier = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'Invocador_Liga'


class InvocadorPartida(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    partida = models.ForeignKey("Partida")
    invocador_id = models.IntegerField(blank=True, null=True)
    campeao_id = models.IntegerField(blank=True, null=True)
    ultimo_tier = models.CharField(max_length=50, blank=True)
    participant_id = models.IntegerField(blank=True, null=True)
    spell = models.IntegerField(blank=True, null=True)
    spell2 = models.IntegerField(blank=True, null=True)
    time_id = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    kills = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    combat_score = models.TextField(blank=True)  # This field type is a guess.
    double_kill = models.IntegerField(blank=True, null=True)
    firstblood_assist = models.IntegerField(blank=True, null=True)
    firstblood_kill = models.IntegerField(blank=True, null=True)
    firsttower_assist = models.IntegerField(blank=True, null=True)
    firsttower_kill = models.IntegerField(blank=True, null=True)
    ouro_ganho = models.TextField(blank=True)  # This field type is a guess.
    ouro_gasto = models.TextField(blank=True)  # This field type is a guess.
    killing_spree = models.IntegerField(blank=True, null=True)
    maior_critico = models.IntegerField(blank=True, null=True)
    maior_ks = models.IntegerField(blank=True, null=True)
    maior_multikill = models.IntegerField(blank=True, null=True)
    danoap_recebido = models.IntegerField(db_column='danoAP_recebido', blank=True, null=True)  # Field name made lowercase.
    danoap_recebido_champs = models.IntegerField(db_column='danoAP_recebido_champs', blank=True, null=True)  # Field name made lowercase.
    danoap_feito = models.IntegerField(db_column='danoAP_feito', blank=True, null=True)  # Field name made lowercase.
    minions_killed = models.IntegerField(blank=True, null=True)
    minions_neutro_killed = models.IntegerField(blank=True, null=True)
    minions_neutro_killed_enemy = models.IntegerField(blank=True, null=True)
    minions_neutro_killed_team = models.IntegerField(blank=True, null=True)
    pentakill = models.IntegerField(blank=True, null=True)
    danoad_recebido = models.IntegerField(db_column='danoAD_recebido', blank=True, null=True)  # Field name made lowercase.
    danoad_recebido_champs = models.IntegerField(db_column='danoAD_recebido_champs', blank=True, null=True)  # Field name made lowercase.
    danoad_feito = models.IntegerField(db_column='danoAD_feito', blank=True, null=True)  # Field name made lowercase.
    quadrakill = models.IntegerField(blank=True, null=True)
    wards = models.IntegerField(blank=True, null=True)
    total_dano_recebido = models.IntegerField(blank=True, null=True)
    total_dano_recebido_champ = models.IntegerField(blank=True, null=True)
    total_dano_feito = models.IntegerField(blank=True, null=True)
    total_cura = models.IntegerField(blank=True, null=True)
    total_tf = models.IntegerField(blank=True, null=True)
    total_unidades_curadas = models.IntegerField(blank=True, null=True)
    torres_deburradas = models.IntegerField(blank=True, null=True)
    triplekill = models.IntegerField(blank=True, null=True)
    dano_verdadeiro_recebido = models.IntegerField(blank=True, null=True)
    dano_verdadeiro_recebido_champ = models.IntegerField(blank=True, null=True)
    dano_verdadeiro_feito = models.IntegerField(blank=True, null=True)
    unrealkill = models.IntegerField(blank=True, null=True)
    pink_wards = models.IntegerField(blank=True, null=True)
    wards_killed = models.IntegerField(blank=True, null=True)
    wards_colocadas = models.IntegerField(blank=True, null=True)
    winner = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Invocador_Partida'


class InvocadorRuna(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    runa_id = models.IntegerField(blank=True, null=True)
    invocador_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Invocador_Runa'


class InvocadorTalento(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    invocador_partida = models.ForeignKey("InvocadorPartida")#models.IntegerField(blank=True, null=True)
    talento_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Invocador_Talento'


class InvocadorTime(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    time_id = models.IntegerField(blank=True, null=True)
    invocador_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Invocador_Time'


class Item(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    item_id = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'Item'


class Liga(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    posicao = models.CharField(max_length=50, blank=True)
    nome = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'Liga'


class Log(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    erro = models.CharField(max_length=100, blank=True)
    data = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Log'


class Mensagem(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    codigo = models.CharField(max_length=50, blank=True)
    mensagem = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'Mensagem'


class Partida(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    mapa_id = models.IntegerField(blank=True, null=True)
    data = models.TextField(blank=True)  # This field type is a guess.
    duracao = models.TextField(blank=True)  # This field type is a guess.
    partida_id = models.IntegerField(blank=True, null=True)
    modo = models.CharField(max_length=50, blank=True)
    tipo = models.CharField(max_length=50, blank=True)
    versao = models.CharField(max_length=50, blank=True)
    plataforma = models.CharField(max_length=50, blank=True)
    queue = models.CharField(max_length=50, blank=True)
    regiao = models.CharField(max_length=50, blank=True)
    season = models.CharField(max_length=50, blank=True)
    data_partida = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Partida'


class Runa(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    runa_id = models.IntegerField(blank=True, null=True)
    field_rank = models.IntegerField(db_column='_rank', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'Runa'


class Skin(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    nome = models.CharField(max_length=100, blank=True)
    img = models.CharField(max_length=100, blank=True)
    campeao_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Skin'


class Statsranked(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    invocador_id = models.IntegerField(blank=True, null=True)
    campeao_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StatsRanked'


class Talento(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    talento_id = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'Talento'


class Time(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    nome = models.CharField(max_length=100, blank=True)
    sigla = models.CharField(max_length=50, blank=True)
    liga_nome = models.CharField(max_length=100, blank=True)
    liga_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Time'


class UsuarioInvocador(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    invocador   = models.ForeignKey('Invocador')
    usuario     = models.ForeignKey('Usuario')
    favorito    = models.IntegerField()
    #ativo = 0
    class Meta:
        managed = False
        db_table = 'Usuario_Invocador'
        
        
class Usuario(models.Model):
    #id = models.IntegerField(primary_key=True, blank=True, null=True)  # AutoField?
    nome  = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100, blank=True)
    senha = models.CharField(max_length=50, blank=True)
    conta_twitch = models.CharField(max_length=100, blank=True)
    conta_facebook = models.CharField(max_length=100, blank=True)
    conta_twitter = models.CharField(max_length=100, blank=True)
    dias_jogo = models.CharField(max_length=255, blank=True)
    horarios_jogo = models.CharField(max_length=255, blank=True)
    invocadores = models.ManyToManyField("Invocador", through='UsuarioInvocador')
    #ativo = 0

    class Meta:
        managed = False
        db_table = 'Usuario'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
