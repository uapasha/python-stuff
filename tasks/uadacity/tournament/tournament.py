#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

###############################################################################
## create supporting class for conection

class DB:
    """
    Class for connecting to database
    """

    def __init__ (self, db_con_str = 'dbname=tournament'):
        """
        Creates a database connection. Connection string can be provided
        as a second(dont forget about 'self') parameter.
        :param str db_con_str: Database connection string. Contains default
        parameter for this particular project - "tournament" database. 
        """
        self.conn = psycopg2.connect(db_con_str)

    def cursor(self):
        """
        Provides cursor object for interaction with DB
        """
        return self.conn.cursor()

    def execute(self, sql_query_string, var_tupl = None, and_close=False):
        """
        Executes sql queries 
        :param srt sql_query_string: Contains the string that will be exucuted
        as a query
        :param tup var_tupl: Contains optional tuples with parameters for
        insertion into query string
        :param bool and_close: Bolean parameter that defines wheather to close
        connection after execution (closes if True)
        """
        cursor = self.cursor()
        cursor.execute(sql_query_string, var_tupl)
        if and_close:
            self.conn.commit()
            self.close()
        return {"conn": self.conn, "cursor": cursor if not and_close else None}

    def close(self):
        """
        closes the current database connection
        """
        return self.conn.close()

###############################################################################

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB().execute("DELETE FROM matches", and_close=True)

def deletePlayers():
    """Remove all the player records from the database."""
    DB().execute("DELETE FROM players", and_close=True)

def countPlayers():
    """Returns the number of players currently registered."""
    conn = DB().execute("SELECT COUNT(id) FROM players")
    count = conn['cursor'].fetchone()[0]
    conn['conn'].close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB().execute("INSERT INTO players (name) values (%s)", (name,), True)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = DB().execute("""
        SELECT * from STANDINGS_VIEW;
        """)
    cursor = conn['cursor']
    res = cursor.fetchall()
    conn['conn'].close()
    return res


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB().execute("""
        INSERT INTO matches 
        VALUES (%s, %s, %s) 
        """, (winner, loser, winner,), True)


 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # use function playerStandings() to acces table with player ratings
    players_list = playerStandings()

    pair =()
    k = 0
    pairs = []

    for i in players_list:

        # create player tuple    
        player = ()
        for n in range (2):
            player = player + (i[n],)

        # add player to pair
        pair = pair + player
        k+=1
        
        # check whether to null pair
        if k % 2 == 0 and pair != ():
            # append pair to result
            pairs.append(pair)
            # null pair
            pair = ()

    return pairs


 


