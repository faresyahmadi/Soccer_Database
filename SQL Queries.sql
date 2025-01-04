
-- Query 1: A query on one table that uses a condition to restrict the rows that are returned from
-- the table.

-- Gets information on goalkeepers in the database
SELECT 
    player_id, 
    player_Name, 
    age, 
    position
FROM 
    player
WHERE 
    position = "Goalkeeper";

-- Query 2: A query that joins two or more tables, plus contains a condition that restricts the rows
-- that are returned from at least one of the tables.

-- Gets transfer infromation on all transfers which were valued at less than 8.0
SELECT 
    TR.transfer_id,
    P.player_Name,
    OT.team_name AS "Old Team",
    CT.team_name AS "New Team",
    TR.transfer_fee, 
    TR.transfer_date
FROM 
    player P
    INNER JOIN
    transfers TR ON P.player_id = TR.player_id
    INNER JOIN
    team OT ON TR.old_team_id = OT.team_id
    INNER JOIN
    team CT ON TR.current_team_id = CT.team_id
WHERE
    TR.transfer_fee < 8.0;
    

-- Query 3: A query that uses a complex condition to restrict the rows that are returned. A complex
-- condition is more than one simple condition with the simple conditions conjoined with AND or
-- OR.

-- Gets players who are younger than 24 and play for English teams
SELECT 
    P.player_Name,
    P.age,
    T.team_name
FROM 
    player P 
    INNER JOIN 
    team T ON P.team_id = T.team_id
    INNER JOIN
    league L ON T.league_id = L.league_id
WHERE 
    (P.age < 24) AND (L.country = 'England');

-- Query 4: A query that includes a result attribute that uses an SQL aggregate function (COUNT,
-- SUM, AVG, MIN, or MAX).

-- Gets the average minuites played by defenders in the database
SELECT 
    AVG(P.mins_played) AS "Average Defender mins"
FROM 
    player P 
WHERE
    P.position = 'Defender';


-- Query 5: A query that has restricted grouped results (using GROUP BY in conjunction with
-- HAVING).

-- Gets players with more than 10 goals and assists
SELECT 
    P.player_Name,
    TR.current_team_id,
    P.goals,
    P.assists,
    TR.transfer_fee
FROM 
    player P
    INNER JOIN
    transfers TR ON P.player_id = TR.player_id
WHERE
    (TR.transfer_fee < 8.0)
GROUP BY
    P.player_Name
HAVING
    SUM(P.goals + P.assists) >= 10;



-- Query 6: A query that requires a sub-query or uses set operators (UNION, INTERSECT, EXCEPT).

-- Gets players who played more than 15 games, excluding goalkeepers
(SELECT 
    P.player_Name,
    P.position,
    P.assists
FROM 
    player P
WHERE 
    P.games_played > 15)
EXCEPT 
(SELECT 
    P.player_Name,
    P.position,
    P.assists
FROM 
    player P
WHERE
    position = 'Goalkeeper');

