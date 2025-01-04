-- Database Design Project Phase 3 Siya Mabuza & Fares Yahmadi

DROP TABLE IF EXISTS transfers;
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;
DROP TABLE IF EXISTS league;

CREATE TABLE league (
    league_id SMALLINT,
    league_name varchar(40) NOT NULL,
    country varchar(10),
    PRIMARY KEY (league_id)
);

CREATE TABLE team (
    team_id SMALLINT,
    team_name varchar(40) NOT NULL,
    league_id SMALLINT,
    PRIMARY KEY (team_id),
    FOREIGN KEY (league_id) REFERENCES league (league_id)
        ON DELETE CASCADE
);


CREATE TABLE player (
    player_id SMALLINT,
    player_Name varchar(60) NOT NULL,
    age SMALLINT NOT NULL,
    position varchar(20) NOT NULL,
    -- height is measured in CM. 
    height SMALLINT NOT NULL,
    -- 1 character L for left and R for right 
    foot CHAR(1) NOT NULL,
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
    team_id SMALLINT,
    PRIMARY KEY (player_id),
    FOREIGN KEY (team_id) REFERENCES team (team_id)
        ON DELETE CASCADE
);


 --how do we show the direction of the transfer, source to current
CREATE TABLE transfers (
    player_id SMALLINT,
    old_team_id SMALLINT,
    current_team_id SMALLINT,
    transfer_id SMALLINT,
    transfer_fee FLOAT,
    transfer_date DATE NOT NULL,
    PRIMARY KEY (player_id, old_team_id, current_team_id, transfer_id),
    FOREIGN KEY (player_id) REFERENCES player (player_id)
        ON DELETE CASCADE,
    FOREIGN KEY (old_team_id) REFERENCES team (team_id)
        ON DELETE CASCADE,
    FOREIGN KEY (current_team_id) REFERENCES team (team_id)
        ON DELETE CASCADE
);
