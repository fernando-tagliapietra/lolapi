/*
CREATE TABLE Usuario(
	id INTEGER PRIMARY KEY AUTOINCREMENT ,
	email varchar(100),
	senha varchar(50),
	conta_twitch varchar(100),
	conta_facebook varchar(100),
	conta_twitter varchar(100),
	dias_jogo varchar(255),
	horarios_jogo varchar(255)
);*/

/*CREATE TABLE Campeao(
	id INTEGER PRIMARY KEY AUTOINCREMENT ,
	campeao_id INTEGER,
	nome VARCHAR(50),
	lane VARCHAR(50)
);*/

/*

CREATE TABLE Runa(
	id INTEGER PRIMARY KEY AUTOINCREMENT ,
	runa_id INTEGER,
	_rank INTEGER
);*/

/*

CREATE TABLE Item(

		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		item_id INTEGER,
		nome VARCHAR(100),
		descricao VARCHAR(255)
);*/


/*

CREATE TABLE Invocador(
		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		api_id INTEGER,
		nome varchar(100),
		tier varchar(50),
		divisao INTEGER,
		icone INTEGER,
		nivel INTEGER,
		regiao varchar(5),
		data_atualizacao TIMESTAMP ,
		liga_nome varchar(50) NULL,
		liga_id INTEGER,
		pdl INTEGER,
		wins INTEGER,
		loses INTEGER,
		series varchar(50)
);*/

/*
CREATE TABLE Invocador_Runa(
	id INTEGER PRIMARY KEY AUTOINCREMENT ,
	runa_id INTEGER,
	invocador_id INTEGER
);*/




/*
CREATE TABLE Usuario_Invocador(
		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		invocador_id INTEGER, 
		usuario_id INTEGER,
		favorito INTEGER,
	
);


	FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
*/



/*

CREATE TABLE Talento(
		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		talento_id INTEGER,
		nome varchar(100)
);*/


/*
CREATE TABLE Partida(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		mapa_id INTEGER,
		data TIMESTAMP ,
		duracao DOUBLE,
		partida_id INTEGER,
		modo VARCHAR(50),
		tipo VARCHAR(50),
		versao VARCHAR(50),
		plataforma VARCHAR(50),
		queue VARCHAR(50),
		regiao VARCHAR(50),
		season VARCHAR(50)
);*/

/*
CREATE TABLE Invocador_Partida(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		partida_id INTEGER,
		invocador_id INTEGER,
		campeao_id INTEGER,
		ultimo_tier VARCHAR(50),
		participant_id INTEGER,
		spell INTEGER,
		spell2 INTEGER,
		time_id INTEGER,
		assists INTEGER,
		kills INTEGER,
		deaths INTEGER,
		level INTEGER,
		combat_score DOUBLE,
		double_kill INTEGER,
		firstblood_assist INTEGER,
		firstblood_kill INTEGER,
		firsttower_assist INTEGER,
		firsttower_kill INTEGER,
		ouro_ganho DOUBLE,
		ouro_gasto DOUBLE,
		killing_spree INTEGER,
		maior_critico INTEGER,
		maior_ks INTEGER,
		maior_multikill INTEGER,
		danoAP_recebido INTEGER,
		danoAP_recebido_champs INTEGER,
		danoAP_feito INTEGER,
		minions_killed INTEGER,
		minions_neutro_killed INTEGER,
		minions_neutro_killed_enemy INTEGER,
		minions_neutro_killed_team INTEGER,
		pentakill INTEGER,
		danoAD_recebido INTEGER,
		danoAD_recebido_champs INTEGER,
		danoAD_feito INTEGER,
		quadrakill INTEGER,
		wards INTEGER,
		total_dano_recebido INTEGER,
		total_dano_recebido_champ INTEGER,
		total_dano_feito INTEGER,
		total_cura INTEGER,
		total_tf INTEGER,
		total_unidades_curadas INTEGER,
		torres_deburradas INTEGER,
		triplekill INTEGER, 
		dano_verdadeiro_recebido INTEGER, 
		dano_verdadeiro_recebido_champ INTEGER,
		dano_verdadeiro_feito INTEGER, 
		unrealkill INTEGER,
		pink_wards INTEGER,
		wards_killed INTEGER,
		wards_colocadas INTEGER, 
		winner INTEGER
		
	
		
);



*/

/*
CREATE TABLE InvocadorPartida_Item(
		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		item_id INTEGER,
		nome VARCHAR(100)
);

*/

/*
CREATE TABLE Invocador_Talento(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		invocador_partida_id INTEGER,
		talento_id INTEGER
	
);

	FOREIGN KEY (talento_id) REFERENCES Talento(id),
		FOREIGN KEY (invocador_partida_id) REFERENCES Invocador_Partida(id)
*/


/*
CREATE TABLE Invocador_Liga(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		invocador_nome VARCHAR(100),
		liga_id INTEGER,
		liga_nome VARCHAR(50),
		tier VARCHAR(50)
);*/

/*
CREATE TABLE Time(
		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		nome VARCHAR(100),
		sigla VARCHAR(50),
		liga_nome VARCHAR(100),
		liga_id INTEGER
);*/

/*
CREATE TABLE Invocador_Time(
		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		time_id INTEGER,
		invocador_id INTEGER
);*/

/*
CREATE TABLE Guia(

		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		usuario_id INTEGER,
		descricao VARCHAR(100),
		html VARCHAR(255),
		votos_positivos INTEGER,
		votos_negativos INTEGER,
		aprovado INTEGER
		
);    FOREIGN KEY (usuario_id) REFERENCES Usuario(id) */



/*
CREATE TABLE StatsRanked(

		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		invocador_id INTEGER,
		campeao_id INTEGER
);*/

/*
CREATE TABLE Skin(
		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		nome VARCHAR(100),
		img VARCHAR(100),
		campeao_id INTEGER
);*/

/*
CREATE TABLE Build(

		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		descricao VARCHAR(50),
		magia1 VARCHAR(50),
		magia2 VARCHAR(50),
		usuario_id INTEGER,
		campeao_id INTEGER,
		temporada INTEGER
		
);

FOREIGN KEY (usuario_id) REFERENCES Usuario(id),
		FOREIGN KEY (campeao_id) REFERENCES Campeao(id)
*/

/*
CREATE TABLE Build_Item(

		id INTEGER PRIMARY KEY AUTOINCREMENT ,
		build_id INTEGER,
		item_id INTEGER
	
);

	FOREIGN KEY (build_id) REFERENCES Build(id),
		FOREIGN KEY (item_id) REFERENCES Item(id)
*/

/*
CREATE TABLE Liga(

		id INTEGER PRIMARY KEY AUTOINCREMENT,
		posicao VARCHAR(50),
		nome VARCHAR(50)
);*/


/*
CREATE TABLE Invocador_Liga(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		invocador_nome VARCHAR(50),
		liga_id INTEGER
		
);

FOREIGN KEY (liga_id) REFERENCES Liga(id)
*/

/*
CREATE TABLE Time(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		time_id INTEGER,
		liga_id INTEGER,
);

		FOREIGN KEY (liga_id) REFERENCES Liga(id)


*/

/*
CREATE TABLE Invocador_Time(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		time_id INTEGER,
		invocador_id INTEGER
);

FOREIGN KEY (time_id) REFERENCES Time(id)
*/

/*
CREATE TABLE Log(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		erro VARCHAR(100),
		data TIMESTAMP 
);*/

/*
CREATE TABLE Mensagem(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		codigo VARCHAR(50),
	    mensagem VARCHAR(100)
);*/