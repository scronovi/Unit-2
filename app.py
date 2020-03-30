import constants

def cleanse_data(**kwargs):
    players = kwargs['players']
    teams = kwargs['teams']
    expTeam = []
    unexpTeam = []

    for player in players:
        for key, value in player.items():
            if key == 'experience' and value == 'YES':
                expTeam.append(player)
            elif key == 'experience' and value == 'NO':
                unexpTeam.append(player)

    if len(expTeam) == len(unexpTeam):
        #1/3 out of expteam and unexpteam to each team
        #check how to get 1/3 of a list, or how to divide a list into 3
        #then append to teams

cleanse_data(players=constants.PLAYERS, teams=constants.TEAMS)

if __name__ == '__main__':
    #main calls / code here
    print('main was called')
