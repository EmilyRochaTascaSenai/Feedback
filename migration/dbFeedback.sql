create database dbFeedback;
use dbFeedback;

create table tbComentarios(
	Nome varchar(100) not null,
   Comentario text not null,
   DataPostagem datetime not null,
   idPostagem  int AUTO_INCREMENT  primary key 
);
