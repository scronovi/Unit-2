import constants

def cleanse_data(**kwargs):
    players = kwargs['players']
    teams = kwargs['teams']
    expTeam = []
    unexpTeam = []

    for player in players.copy():
        for key, value in player.items():
            if key == 'experience' and value == 'YES':
                expTeam.append(player)
            elif key == 'experience' and value == 'NO':
                unexpTeam.append(player)

if __name__ == '__main__':
    #main calls / code here
    print('main was called')
