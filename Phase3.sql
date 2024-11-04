-- Database Design Project Phase 3 Siya Mabuza & Fares Yahmadi

DROP TABLE IF EXISTS participates_in;
DROP TABLE IF EXISTS transfers;
DROP TABLE IF EXISTS belongs_to;
DROP TABLE IF EXISTS league;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS player;

CREATE TABLE player (
    player_id varchar(10),
    player_Name varchar(20),
    age SMALLINT,
    position varchar(20),
    height SMALLINT,
    -- 1 character L for left and R for right 
    foot CHAR(1),
    transfer_price SMALLINT,
    goals SMALLINT,
    assists SMALLINT,
    games_played SMALLINT,
    mins_played SMALLINT,
    total_shots SMALLINT,
    shots_on_target SMALLINT,
    total_passes SMALLINT,
    successful_passes SMALLINT,
    total_tackles SMALLINT,
    successful_tackles SMALLINT,
    clean_sheets SMALLINT,
    saves SMALLINT,
    PRIMARY KEY (player_id)
);

CREATE TABLE team (
    team_id varchar(10),
    team_name varchar(40),
    team_location varchar(20),
    team_size SMALLINT,
    PRIMARY KEY (team_id)
);

CREATE TABLE league (
    league_id varchar(8),
    league_name varchar(40),
    country varchar(10),
    PRIMARY KEY (league_id)
);

CREATE TABLE belongs_to (
    player_id varchar(10),
    team_id varchar(10),
    PRIMARY KEY (player_id, team_id),
    FOREIGN KEY (player_id) REFERENCES player (player_id)
        ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES team (team_id)
        ON DELETE CASCADE
);

 --how do we show the direction of the transfer, source to destination
CREATE TABLE transfers (
    player_id varchar(10),
    team_id varchar(10),
    transfer_id varchar(5),
    transfer_fee FLOAT,
    transfer_date DATE,
    PRIMARY KEY (player_id, team_id),
    FOREIGN KEY (player_id) REFERENCES player (player_id)
        ON DELETE CASCADE,
    FOREIGN KEY (team_id) REFERENCES team (team_id)
        ON DELETE CASCADE
);

CREATE TABLE participates_in (
    team_id varchar(10),
    league_id varchar(8),
    PRIMARY KEY (team_id, league_id),
    FOREIGN KEY (team_id) REFERENCES team (team_id)
        ON DELETE CASCADE,
    FOREIGN KEY (league_id) REFERENCES league (league_id)
        ON DELETE CASCADE
);




insert into player values ('31649', 'Fares Yahmadi', '23','Right Back',184, 'R', 0, 6, 4, 5, 360, 16, 7, 38, 28, 7, 7, 0, 0);
insert into player values ('12345', 'John Smith', 25, 'Striker', '185', 'R', 1500, 10, 4, 12, 920, 40, 150, 10, 20, 120, 8, 4, 0);
insert into player values ('23456', 'Leo Martinez', 22, 'Midfielder', '177', 'L', 2000, 6, 7, 15, 1200, 30, 280, 18, 10, 250, 12, 3, 0);
insert into player values ('34567', 'Kofi Mensah', 28, 'Defender', '182', 'R', 800, 2, 1, 18, 1620, 15, 300, 35, 5, 190, 30, 7, 0);
insert into player values ('45678', 'Ahmed Omar', 30, 'Goalkeeper', '188', 'R', 3000, 0, 0, 18, 1620, 1, 50, 5, 1, 40, 0, 14, 10);
insert into player values ('56789', 'Marcus Chan', 21, 'Winger', '173', 'L', 1200, 8, 5, 10, 800, 25, 140, 8, 15, 100, 6, 2, 0);
insert into player values ('67890', 'Alex Dupont', 26, 'Midfielder', '180', 'R', 1800, 4, 9, 14, 1100, 20, 260, 20, 8, 230, 15,5, 0);
insert into player values ('78901', 'Yuki Nakamura', 24, 'Defender', '179', 'L', 900, 1, 2, 16, 1400, 10, 280, 28, 4, 200, 22, 10, 0);
insert into player values ('89012', 'Carlos Diaz', 29, 'Striker', '185', 'R', 2500, 15, 6, 19, 1700, 55, 120, 12, 35, 100, 5, 1, 0);
insert into player values ('90123', 'Max Svensson', 23, 'Goalkeeper', '190', 'R', 4000, 0, 0, 15, 1350, 2, 60, 4, 0, 55, 0, 12, 15);
insert into player values ('01234', 'Brahim El-Khatib', 27, 'Winger', '178', 'L', 1700, 7, 8, 13, 1050, 30, 210, 14, 20, 180, 9, 3, 0);
insert into player values ('11223', 'Liam Gallagher', 22, 'Defender', '183', 'R', 1000, 2, 3, 17, 1500, 12, 290, 32, 3, 220, 28, 9, 0);



insert into team values ('E111', 'Liverpool FC', 'Liverpool', '35');
insert into team values ('E001', 'Manchester United FC', 'Manchester', '34');
insert into team values ('E547', 'Arsenal FC', 'London', '38');
insert into team values ('E795', 'Brighton FC', 'East Sussex', '31');
insert into team values ('E698', 'Tottenham Spurs FC', 'North London', '35');
insert into team values ('E458', 'Manchester City FC', 'Manchester', '40');
insert into team values ('F131', 'Paris Saint Germain FC', 'Paris', '35');
insert into team values ('F001', 'Monaco FC', 'Monaco', '34');
insert into team values ('F547', 'Lille FC', 'Lille', '37');
insert into team values ('G795', 'Dortmund FC', 'Dortmund', '30');
insert into team values ('G451', 'Bayern Munich FC', 'Munich', '33');
insert into team values ('S991', 'FC Barcelona', 'Barcelona', '42');
insert into team values ('I811', 'AC Milano', 'Milano', '44');


insert into league values ('0001', 'U20 Premiere League', 'England');
insert into league values ('0010', 'U21 Super Leage', 'France');
insert into league values ('0011', 'U19 German ProLeague', 'Germany');
insert into league values ('0100', 'U20 Italian League', 'Italy');
insert into league values ('0101', 'U20 Spanish League', 'Spain');



insert into belongs_to values ('31649', 'E001');
insert into belongs_to values ('12345', 'E111');
insert into belongs_to values ('23456', 'E547');
insert into belongs_to values ('34567', 'E795');
insert into belongs_to values ('45678','F131');
insert into belongs_to values ('56789','F001');
insert into belongs_to values ('67890','G795');
insert into belongs_to values ('78901','G451') ;
insert into belongs_to values ('89012','G451');
insert into belongs_to values ('90123','S991');
insert into belongs_to values ('01234','I811') ;
insert into belongs_to values ('11223','E698');



insert into transfers values ('34567', 'E795','951',9.5, 03/05/2023);
insert into transfers values ('45678','F131','753',8.2, 02/08/2023);
insert into transfers values ('56789','F001','456',7.1, 07/11/2023);
insert into transfers values ('67890','G795','852',4.3, 04/12/2023);
insert into transfers values ('78901','G451','684',10.6, 01/17/2023) ;
insert into transfers values ('89012','G451','426',2.5, 12/31/2023);



insert into participates_in values ('E111','0001');
insert into participates_in values ('E001','0001');
insert into participates_in values ('E547','0001');
insert into participates_in values ('E795','0001');
insert into participates_in values ('E698','0001');
insert into participates_in values ('E458','0001');
insert into participates_in values ('E131','0001');
insert into participates_in values ('F001','0010');
insert into participates_in values ('F547','0010');
insert into participates_in values ('G795','0011');
insert into participates_in values ('G451','0011');
insert into participates_in values ('S991','0100');
insert into participates_in values ('I811','0101');
