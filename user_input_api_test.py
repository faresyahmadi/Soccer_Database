from football_api import FootballScoutingAPI

def main():
    foot_api = FootballScoutingAPI()
    
    print() 
    
    
    #query 1
    print('This is query 1')
    print('Gets information on players in specific posistions in the database')
    position = input("Enter a postion (Attacker, Midfielder, Defender, Goalkeeper): ").lower()
    resullt = foot_api.run_q1(position)
    for row in resullt:
        print('player_id: ', row[0], '; Name: ', row[1], '; Age:', row[2], '; Position:', row[3])

    #query 2
    
    print('This is query 2')
    print('Gets transfer infromation on all transfers which were valued at less than a certain value')
    transfer_fee = input("Enter a value for transfer fee: ")
    result2 = foot_api.run_q2(transfer_fee)
    for row in result2:
        print('Transfer ID: ', row[0], '; Player Name: ', row[1], '; Old Team:', row[2], '; New Team:', row[3], ';Transfer Price:' , row[4],';TR.transfer_date:' , row[5])


    #query 3
    print('This is query 3')
    print('Gets players who are younger than a certain age and play for teams in given country')
    age = input("Enter a value for age: ")
    country = input("Enter a country (England, Spain, France, Germany, Italy): ").lower()
    result3 = foot_api.run_q3(age, country)
    for row in result3:
        print('Player Name: ', row[0], '; Age: ', row[1], '; Team Name:', row[2])



    #query 4
    print('This is query 4')
    print('Gets the average minuites played by players in specific posistion in the database')
    position = input("Enter a postion (Attacker, Midfielder, Defender, Goalkeeper): ").lower()
    result4 = foot_api.run_q4(position)
    for row in result4:
        print('Average minutes played by a defender: ', row)

    
    #query 5
    print('This is query 5')
    print('Gets players with more than a certain amount of goals and assists and have a transfer fee less than a certain amount: ')
    transfer_fee_1 = input("Enter a value for transfer fee (Between 10-100): ")
    goals_assists = input("Enter a value for the sum of goals and assists: ")
    result5 = foot_api.run_q5(transfer_fee_1, goals_assists)
    for row in result5:
        print(' Player Name: ', row[0], '; Current Team ID:', row[1], '; Goals:', row[2], '; Assists:' , row[3],'; Transfer Price :' , row[4])

    #query 6
    print('This is query 6')
    print('Gets players who played more than x games, excluding certain posistion')
    games_played = input('Enter the amount of games played (between 10-50): ')
    position = input("Enter a postion (Attacker, Midfielder, Defender, Goalkeeper): ").lower()
    result6 = foot_api.run_q6(games_played, position)
    for row in result6:
        print(' Player Name: ', row[0], '; Position:', row[1], '; Assists:', row[2])

    print("End of test queries. :)")

if __name__ == '__main__':
    main()