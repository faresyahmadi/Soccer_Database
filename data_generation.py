import random
from faker import Faker
import mariadb
import sys
import random


dbName = "siyamabuza_sandbox"
# Database username
dbUser = "siyamabuza"
# Database password
dbPass = "pass4543"

#used to generate fake names for all the players
fake = Faker()

#funtion used to get ids from given tables in our database
def get_ids_from_db(query, db_cur):
    db_cur.execute(query)
    # Put the ids into a list
    id_list = []
    for (row) in db_cur:
        id_list.append(row[0])
    
    return id_list

#function used to generate 27 players in a given team.
#generates only infield players (defenders, midfielder, attackers) because each 
#generated player is randomly assigned a position. 
#Teams tend to have very few goalkeepers so we make goalkeeper generation its own function
def generate_players(x,db_cur,team_id):  #take in league id so we create players per league?

    data = []
    for player_id in range(x, x+27):
        player_name = fake.name()
        age = random.randint(15, 23)  # Random age between 18 and 40
        position = random.choice(['Defender', 'Midfielder', 'Forward'])
        height = random.randint(160, 200)  # Height in cm
        foot = random.choice(['L', 'R'])
        #get realitic goals based off of the position played
        if position == 'Defender':
            goals = random.randint(0, 5)
        elif position == 'Midfielder':
            goals = random.randint(0, 15)
        elif position == 'Attacker':
            goals = random.randint(0, 40)
        else:
            goals = 0
        #get realitic assists based off of the position played
        if position == 'Defender':
            assists = random.randint(0, 5)
        elif position == 'Midfielder':
            assists = random.randint(0, 30)
        elif position == 'Attacker':
            assists = random.randint(0, 20)
        else:
            assists = 0
        games_played = random.randint(10, 50)
        mins_played = games_played * random.randint(20, 90)  # Minutes played per game
        if position in ['Midfielder', 'Forward']:
            total_shots = random.randint(3, 100)
        elif position == 'Defender':
            total_shots = random.randint(3, 20)
        else:
            total_shots = 0
        shots_on_target = random.randint(0, total_shots - 3) if total_shots else 0
        #get realitic passes based off of the position played
        if position in ['Midfielder', 'Defender']:
            total_passes = random.randint(500, 2500)
        elif position == 'Attacker':
            total_passes = random.randint(500, 1500)
        else:
            total_passes = random.randint(10, 500)
        successful_passes = random.randint(0, total_passes - 8)
        #get realitic tackles based off of the position played
        if position in ['Midfielder', 'Defender']:
            total_tackles = random.randint(20, 150)
        elif position == 'Attacker':
            total_tackles = random.randint(2, 30)
        else:
            total_tackles = 0
        successful_tackles = random.randint(0, total_tackles) if total_tackles else 0
        clean_sheets = 0
        saves = 0
        
        
        data.append((player_id, player_name, age, position, height, foot, goals,
                    assists, games_played, mins_played, total_shots, shots_on_target,
                    total_passes, successful_passes, total_tackles,
                    successful_tackles, clean_sheets, saves, team_id))
        insert_statement = 'INSERT INTO player (player_id, player_name, '
        insert_statement += 'age, position, height, foot, goals,assists, '
        insert_statement += 'games_played, mins_played, total_shots, shots_on_target, '
        insert_statement += 'total_passes, successful_passes, total_tackles, '
        insert_statement += 'successful_tackles, clean_sheets, saves, team_id) '
        insert_statement += 'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    db_cur.executemany(insert_statement,data)

#funtion used to generate 3 goalkeepers for a given team. 
def generate_goalkeepers(x,db_cur, team_id):
    data=[]
    for player_id in range(x+27,x+30):
        player_name = fake.name()
        age = random.randint(15, 23)  # Random age between 18 and 40
        position = 'Goalkeeper'
        height = random.randint(175, 200)  # Height in cm
        foot = random.choice(['L', 'R'])
        goals = 0
        assists = random.randint(0, 3)
        games_played = random.randint(10, 50)
        mins_played = games_played * random.randint(20, 90)  # Minutes played per game
        total_shots = 0
        shots_on_target = random.randint(0, total_shots - 3) if total_shots else 0
        total_passes = random.randint(10, 500)
        successful_passes = random.randint(0, total_passes - 8)
        total_tackles = random.randint(0, 5) 
        successful_tackles = random.randint(0, total_tackles) if total_tackles else 0
        clean_sheets = random.randint(0, games_played) if position == 'Goalkeeper' else 0
        saves = random.randint(0, 100) if position == 'Goalkeeper' else 0


        data.append((player_id, player_name, age, position, height, foot, goals,
                    assists, games_played, mins_played, total_shots, shots_on_target,
                    total_passes, successful_passes, total_tackles,
                    successful_tackles, clean_sheets, saves, team_id))
        insert_statement = 'INSERT INTO player (player_id, player_name, '
        insert_statement += 'age, position, height, foot, goals,assists, '
        insert_statement += 'games_played, mins_played, total_shots, shots_on_target, '
        insert_statement += 'total_passes, successful_passes, total_tackles, '
        insert_statement += 'successful_tackles, clean_sheets, saves, team_id) '
        insert_statement += 'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    db_cur.executemany(insert_statement,data)



#funtion used to generate the leagues. Takes in the helper array above
def generate_leagues(leagues_array, db_cur): 
    league_list =[]
    for l in leagues_array:
        league_list.append((l[0], l[1], l[2]))
    insert_statement = 'INSERT INTO league (league_id, league_name, country) VALUES (?,?,?)'
    db_cur.executemany(insert_statement,league_list) 

#generates the teams in each league, using the league arrays initialized at the top of this file
def generate_team(teams, team_id, league_id,db_cur):
    team_list =[]
    for i in range(len(teams)):
        team_name = teams[i]
        team_list.append((team_id, team_name, league_id))  
        team_id += 1
        insert_statement = 'INSERT INTO team (team_id, team_name, league_id) VALUES (?,?,?)'
    db_cur.executemany(insert_statement,team_list)  

#function used to randomly transfer players in our database to other teams. takes in the number of transfers we want to make
def generate_transfer(x,db_cur):
    transfer_list = []
    transfer_id = 0
    for i in range (x):
        old_team_id = get_ids_from_db('SELECT team_id FROM team ORDER BY RAND() LIMIT 1', db_cur)
        current_team_id = get_ids_from_db('SELECT team_id FROM team ORDER BY RAND() LIMIT 1', db_cur)
        # while old_team_id == current_team_id: #ensure player is getting transfered to a new team
        #     current_team_id = get_ids_from_db('SELECT team_id FROM team ORDER BY RAND() LIMIT 1', db_cur)
        random_player_id = random.randint(0, 2880)
        transfer_id += 1
        day = random.randint(1,28)
        month = random.randint(1,12)
        random_date = '2024-' + str(month) + '-' + str(day)
        transfer_fee = round(random.uniform(8.5,100.6), 2)
        transfer_list.append((random_player_id,old_team_id[0], current_team_id[0], transfer_id, transfer_fee, random_date))
        insert_statement = 'INSERT INTO transfers (player_id, old_team_id, current_team_id, transfer_id, transfer_fee, transfer_date) VALUES (?,?,?,?,?,?)'
        #print(transfer_list)
    db_cur.executemany(insert_statement,transfer_list)  


def main(): 
    print('connecting to db')
    try:
        conn = mariadb.connect(
            user = dbUser,
            password = dbPass,
            host="cslab.skidmore.edu",
            port=3306,
            database=dbName)
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Create a database cursor for interacting with the database
    cur = conn.cursor()

    #Arrays with all the team names from the top 5 European Soccer Leagues
    epl_teams = [
        "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton & Hove Albion",
        "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Liverpool", "Luton Town",
        "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sheffield United",
        "Tottenham Hotspur", "West Ham United", "Wolverhampton Wanderers"
    ]

    la_liga_teams = [
        "Alavés", "Athletic Club", "Atlético Madrid", "Barcelona", "Real Betis",
        "Celta Vigo", "Espanyol", "Getafe", "Girona", "Las Palmas",
        "Leganés", "Mallorca", "Osasuna", "Real Sociedad", "Rayo Vallecano",
        "Real Madrid", "Valladolid", "Sevilla", "Valencia", "Villarreal"
    ]

    serie_a_teams = [
        "AC Milan", "Atalanta", "Bologna", "Cagliari", "Como", "Empoli", "Fiorentina",
        "Genoa", "Inter Milan", "Juventus", "Lazio", "Lecce", "Monza","Napoli", "Parma",
        "Roma", "Torino", "Udinese", "Venezia", "Verona"
    ]

    bundesliga_teams = [
        '1. FC Heidenheim', '1. FC Union Berlin', '1. FSV Mainz 05', 'Bayer Leverkusen', 
        'Bayern Munich', 'Borussia Dortmund', 'Borussia Mönchengladbach', 
        'Eintracht Frankfurt', 'FC Augsburg', 'FC St. Pauli', 'Holstein Kiel', 
        'RB Leipzig', 'SC Freiburg', 'TSG Hoffenheim', 'VfB Stuttgart', 'VfL Bochum',
        'VfL Wolfsburg', 'Werder Bremen'
    ]

    ligue_1_teams = [
        'AJ Auxerre', 'AS Monaco', 'AS Saint-Étienne', 'Angers SCO', 'FC Nantes', 
        'Le Havre AC', 'Lille OSC', 'Montpellier HSC', 'OGC Nice', 'Olympique Lyonnais', 
        'Olympique de Marseille', 'Paris Saint-Germain', 'RC Lens', 'RC Strasbourg', 
        'Stade Brestois 29', 'Stade Rennais', 'Stade de Reims', 'Toulouse FC'
    ]


    #helper array used as the paramerter in the league generation funtion.
    #since there are only 5 league, league ids are given in the helper array below.
    leagues = [(1, "Bundesliga", "Germnay"), 
                (2, "Ligue1", "France"), 
                (3, "EPL", "England"),
                (4, "SERIE A", "Italy"), 
                (5, "La Ligua", "Spain")]#(league_id, league_name, country)
    
    #uses leagues helper array to generate the 5 leagues
    generate_leagues(leagues, cur)

    #since there are 5 leagues with 5 different ids, get each specific id and generate the teams for that league
    #using the appropriate array holding the teams in that league, and a starting index to ensure all teams have a unique id
    league_ids = get_ids_from_db('SELECT league_id FROM league', cur)
    for id in league_ids: 
        if id == 1:
            generate_team(bundesliga_teams,100,id,cur)
        elif id == 2:
            generate_team(ligue_1_teams,200,id,cur)
        elif id == 3:
            generate_team(epl_teams,300,id,cur)
        elif id == 4:
            generate_team(serie_a_teams,400,id,cur)
        elif id == 5:
            generate_team(la_liga_teams,500,id,cur)
        else: 
            print("Error generating teams")


    #generate 30 players for every team (27 infield players + 3 goalkeepers)
    team_id = get_ids_from_db('SELECT team_id FROM team', cur)
    count1 = 0
    for id in team_id: 
        generate_goalkeepers(count1,cur,id)
        generate_players(count1,cur,id)
        count1 += 30

    #randomly transfers 600 players from one team to anoother
    generate_transfer(600,cur)

    conn.commit()

    cur.close()
    print('Closed cursor')

    # Close the database connection
    conn.close()
    print('Closed database connection')
# end of main function

# Tell the Python interpreter to begin execution at the main function
if __name__ == '__main__':
    main()

