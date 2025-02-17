create database cineflix;

use cineflix;

create table usuarios (
id int auto_increment primary key,
username varchar(100) not null,
senha varchar(20) not null,
email varchar(200) not null,
data_criacao datetime default current_timestamp,
ultimo_login datetime default current_timestamp,
tipo enum('admin','usuario') default 'usuario'
);

create table assinaturas (
id int auto_increment primary key,
id_usuario int not null,
data_inicial datetime,
data_final datetime,
foreign key (id_usuario) references usuarios(id)
);

create table series_filmes (
id int auto_increment primary key,
titulo varchar(255) not null,
genero varchar(55) not null,
data_lancamento date,
duracao int -- em minutos
);

create table historico (
id int auto_increment primary key,
id_usuario int not null,
id_filme int not null,
data_visualizacao datetime default current_timestamp,
progresso int, -- aonde o cara parou de assistir
foreign key (id_usuario) references usuarios(id),
foreign key (id_filme) references series_filmes(id)
);

create table recomendacao (
id int auto_increment primary key,
id_usuario int not null,
id_filme int not null,
nota decimal(3, 2), -- uma nota ate 5 para o filme
foreign key (id_usuario) references usuarios(id),
foreign key (id_filme) references series_filmes(id)
);