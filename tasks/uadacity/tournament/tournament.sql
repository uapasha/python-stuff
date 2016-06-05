-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

-- create database
create database tournament;

-- connect to database
\c tournament;

-- create tables

CREATE TABLE players (id serial PRIMARY KEY, name text);

CREATE TABLE matches (
			player1 integer, 
			player2 integer, 
			won integer
			);

-- create supporting views

CREATE VIEW GAMES_VIEW AS 
    SELECT a.id, sum(a.games) as games 
    FROM (
   	 	SELECT player1 as id, count(player1) as games
    	FROM matches
    	GROUP BY id
    	UNION 
    	SELECT player2 as id, count(player2) as games
    	FROM matches
    	GROUP BY id
    	) as a
    GROUP BY a.id;

CREATE VIEW WINS_VIEW AS
	SELECT players.id as id, count(*) as wins
    FROM players
    JOIN matches
    ON matches.won = players.id
    GROUP BY id;


-- create view for standings
CREATE VIEW STANDINGS_VIEW AS
    SELECT players.id as id, players.name as name, 
    COALESCE(gwin.wins, 0) as wins, COALESCE (ngames.games, 0) as matches
    FROM players
    LEFT JOIN GAMES_VIEW  as ngames
    ON players.id = ngames.id
    LEFT JOIN WINS_VIEW as gwin
    ON players.id = gwin.id
    ORDER BY wins DESC;

-- return to home database
\c vagrant

