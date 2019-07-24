import sqlite3
connection_object = sqlite3.connect("pro.db") #Connection IP
cursor_object = connection_object.cursor()


cursor_object.execute("create table membersignup(name varchar(25) not null,sapid varchar(9) check (sapid like'5000%'),password varchar(12),registration_num varchar(12) not null,stuchapterID varchar(10),branch varchar(15) not null,yearofstudy number check (yearofstudy in (1,2,3,4)) not null,gender varchar(1) check (gender in ('m','M','F','f','o','O')) not null,memberfee int check (memberfee in (500,1000,2000)) not null,primary key (sapid,password));")



cursor_object.execute("create table committee(comm_name varchar (20) primary key,founder_name varchar (25),president_name varcahr (25),foreign key (founder_name) references membersignup(name),foreign key (president_name) references membersignup(name));")


cursor_object.execute("create table goals(comm_name varchar(20),goals varchar(100) primary key,foreign key (comm_name) references committee(comm_name));")

cursor_object.execute("create table positions(position varchar(15) primary key);")

cursor_object.execute("create table committee_members(comm_name varchar(20),member_name varchar(25),position varchar(15),primary key (comm_name,member_name,position),foreign key (comm_name) references committee(comm_name),foreign key(member_name) references membersignup(name),foreign key (position) references positions(position));")


cursor_object.execute("create table events(event_name varchar(20) primary key,judge varchar(20),prize_money decimal (5,2),conducting_comm varchar(20),foreign key (conducting_comm) references committee(comm_name));")

cursor_object.execute("create table participation(event_name varchar(20),group_name varchar(20) primary key,fees decimal(5,2),foreign key (event_name) references events(event_name));")

cursor_object.execute("create table participation_members(group_name varchar(20),member_name varchar(25),member_sapid varchar(9),foreign key (group_name) references participation(group_name));")
