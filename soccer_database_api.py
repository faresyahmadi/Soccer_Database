import mariadb
import sys

# NOTE: it is not best practice to include the database login information
# in the code file. We are using this approach for convenience.


# Name of the database
dbName = "siyamabuza_sandbox"

# Database username
dbUser = "siyamabuza"

# Database password
dbPass = "pass4543"

# Query 1: A query on one table that uses a condition to restrict the rows that are returned from
# the table.

# Gets information on players in specific posistions in the database
query1_str = 'SELECT player_id, player_name, age, position '
query1_str += 'FROM player '
query1_str += 'WHERE position = ?'

# Query 2: A query that joins two or more tables, plus contains a condition that restricts the rows
# that are returned from at least one of the tables.

# Gets transfer infromation on all transfers which were valued at less than a certain value
query2_str = 'SELECT TR.transfer_id, P.player_name, OT.team_name AS "Old Team", CT.team_name AS "New Team", TR.transfer_fee,  TR.transfer_date '
query2_str += 'FROM player P INNER JOIN transfers TR ON P.player_id = TR.player_id INNER JOIN team OT ON TR.old_team_id = OT.team_id INNER JOIN team CT ON TR.current_team_id = CT.team_id '
query2_str += 'WHERE TR.transfer_fee < ?'
    

# Query 3: A query that uses a complex condition to restrict the rows that are returned. A complex
# condition is more than one simple condition with the simple conditions conjoined with AND or
# OR.

# Gets players who are younger than a certain age and play for teams in given country
query3_str = 'SELECT P.player_name, P.age, T.team_name '
query3_str += 'FROM player P INNER JOIN team T ON P.team_id = T.team_id INNER JOIN league L ON T.league_id = L.league_id '
query3_str += 'WHERE (P.age <= ?) AND (L.country = ?)'

# Query 4: A query that includes a result attribute that uses an SQL aggregate function (COUNT,
# SUM, AVG, MIN, or MAX).

# Gets the average minuites played by players in specific posistion in the database
query4_str = 'SELECT AVG(P.mins_played) '
query4_str += 'FROM player P '
query4_str += 'WHERE P.position = ?'


# Query 5: A query that has restricted grouped results (using GROUP BY in conjunction with
# HAVING).

# Gets players with more than 10 goals and assists
query5_str = 'SELECT P.player_name, TR.current_team_id, P.goals, P.assists, TR.transfer_fee '
query5_str += 'FROM player P INNER JOIN transfers TR ON P.player_id = TR.player_id '
query5_str += 'WHERE TR.transfer_fee < ? '
query5_str += 'GROUP BY P.player_Name '
query5_str += 'HAVING SUM(P.goals + P.assists) >= ?'



# Query 6: A query that requires a sub-query or uses set operators (UNION, INTERSECT, EXCEPT).

# Gets players who played more than x games, excluding certain posistion
query6_str = '(SELECT P.player_name, P.position, P.assists '
query6_str += 'FROM player P '
query6_str += 'WHERE P.games_played > ?) '
query6_str += 'EXCEPT (SELECT P.player_name, P.position, P.assists '
query6_str += 'FROM player P '
query6_str += 'WHERE P.position = ?)'


class FootballScoutingAPI:
    
    # init function creates the database connection and creates a cursor object
    # for each query that is part of this API   
    def __init__(self):
        # Open the database connection
        print('connecting to db')
        try:
            self.conn = mariadb.connect(
                user = dbUser,
                password = dbPass,
                host="cslab.skidmore.edu",
                port=3306,
                database=dbName)
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
            
        self.query1_cur = self.conn.cursor(prepared=True)
        self.query2_cur = self.conn.cursor(prepared=True)
        self.query3_cur = self.conn.cursor(prepared=True)
        self.query4_cur = self.conn.cursor(prepared=True)
        self.query5_cur = self.conn.cursor(prepared=True)
        self.query6_cur = self.conn.cursor(prepared=True)
        
    def clost(self):
        self.query1_cur.close()
        self.query2_cur.close()
        self.query3_cur.close()
        self.query4_cur.close()
        self.query5_cur.close()
        self.query6_cur.close()
        self.conn.close()
        print('Database connection is closed')
        
    # Function runs query 1 using the provided posistion as the parameter
    # Returns a list of players in that posistion
    def run_q1(self, position):
        self.query1_cur.execute(query1_str, (position,))
        
        players = []
        for (row) in self.query1_cur:
            #(player_id, player_name, age, position)
            players.append((row[0], row[1], row[2], row[3])) 
            
        return players
    
    # Function runs query 2 using the provided transfer value as the parameter
    # Returns a list of players valued less than provided value
    def run_q2(self, price):
        self.query2_cur.execute(query2_str, (price,))
        
        transfers = []
        for (row) in self.query2_cur:
            # (transfer_id, player_name, old team, new team, fee, tranfer date)
            transfers.append((row[0], row[1], row[2], row[3], row[4], row[5])) 
            
        return transfers
    
    
    # Function runs query 3 using age and country as the parameter to filter data
    # Returns a list of player name, ages and teams of players younger than given age in the given country
    def run_q3(self, age, country):
        self.query3_cur.execute(query3_str, (age, country,))
        
        players = []
        for (row) in self.query3_cur:
            # (player name, age, team)
            players.append((row[0], row[1], row[2])) 
            
        return players
    
    
    # Function runs query 4 using posistion as the parameter 
    # Returns a list of average minutesplayed in given position
    def run_q4(self, position):
        self.query4_cur.execute(query4_str, (position,))
        
        players = []
        for (row) in self.query4_cur:
            # (player name, age, team)
            players.append((row[0])) 
            
        return players
    
    # Function runs query 5 using min tranfer fee and goals+assist value
    # Returns a list of players who cost less than given fee and have a certain goal+assist minimum
    def run_q5(self, min_fee, min_GA):
        self.query5_cur.execute(query5_str, (min_fee, min_GA,))
        
        players = []
        for (row) in self.query5_cur:
            # (player name, curr_team, goals, assists, transfer fee)
            players.append((row[0], row[1], row[2], row[3], row[4]))
            
        return players
    
    # Function runs query 6 using x games played and posistion
    # Returns a list of players and their assists who have played atleast x games and play given position
    def run_q6(self, num_games, position):
        self.query6_cur.execute(query6_str, (num_games, position,))
        
        players = []
        for (row) in self.query6_cur:
            # (player name, curr_team, goals, assists, transfer fee)
            players.append((row[0], row[1], row[2]))
            
        return players