import constants
import time

def clean_data(**kwargs):
    players = kwargs['players']
    teams = kwargs['teams']

    total_players = len(players)
    total_teams = len(teams)

    team_list = {team: [] for team in teams}
    avg_team_size = (total_players // total_teams)

    #Cast experience as bool and height as int
    for player in players.copy():

        for k, v in list(player.items()):
            if k == 'experience' and v == 'YES':
                player[k] = bool(player[k])
                player[v] = True
            elif k == 'height':
                player_height = v.split(' ')
                player[v] = int(player_height[0])
                print(player[v])

    for name, val in team_list.items():

        for player in players.copy():
            #Check how many players are in the current selected team from team list
            #Append player if playercount < (total_players // total_teams)
            #Remove player from players copy when appended
            if len(team_list[name]) < (avg_team_size):
                team_list[name].append(player)
                players.remove(player)

    return team_list


cleaned_data = clean_data(players=constants.PLAYERS, teams=constants.TEAMS)
print()

# EXAMPLE------
# BASKETBALL TEAM STATS TOOL
#
# ---- MENU ----
#
#     Here are your choices:
#     1) Display team stats
#     2) Quit
#
# Enter an option:


def show_data(data, option):
    name = [k['name'] for k in data[option]]
    print('\nTeam {}:'.format(option))
    print('--------------------')
    print('\nPlayers on team:\n{}'.format(', '.join(name)))
    print('Playercount: {}'.format(len(data[option])))


def main_menu():
    print('\nBASKETBALL TEAM STATS TOOL')
    print('\n---- MENU ----')
    user_input = input('\nPlease choose an option: \n1. Display team stats\n2. Quit\n\n')

    user_input
    if user_input == '1':
        teams_choice = input('\n1. Panthers\n2. Bandits\n3. Warriors\n\n')
        teams_choice
        if teams_choice == '1':
            #show Panthers info
            #JOIN Names of the players in the team (first & last?)
            #Total number of players on that team
            show_data(cleaned_data, 'Panthers')
        elif teams_choice == '2':
            #show Bandits info
            show_data(cleaned_data, 'Bandits')
        elif teams_choice == '3':
            #show warriors info
            show_data(cleaned_data, 'Warriors')

    elif user_input == '2':
        print('Basketball team stats tool will quit.')
        time.sleep(0.5)
        quit()


if __name__ == '__main__':
    main_menu()