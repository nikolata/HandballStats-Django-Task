
from collections import defaultdict
import itertools


class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.opponents = []

    def add_win(self):
        self.wins += 1

    def append_opponent(self, opponent):
        self.opponents.append(opponent)

    def __str__(self):
        return f'{self.name}' + '\n' + f' - Wins: {self.wins}' + '\n' \
            + f' - Opponents: {", ".join(sorted(self.opponents))}'


def team_is_winner(left_score, right_score):
    points_left_team = int(left_score.split(":")[0]) + int(right_score.split(":")[1])
    points_right_team = int(left_score.split(":")[1]) + int(right_score.split(":")[0])
    if points_left_team > points_right_team:
        return True
    if points_right_team == points_left_team and int(right_score.split(":")[1]) > int(left_score.split(":")[1]):
        return True
    return False


def store_info_from_input(first_team, second_team, first_game, second_game, viewed_teams, teams):
    if first_team not in viewed_teams:
        viewed_teams.append(first_team)
        temp = Team(first_team)
        temp.append_opponent(second_team)
        if team_is_winner(first_game, second_game):
            temp.add_win()
        teams.append(temp)
    else:
        for team in teams:
            if team.name == first_team:
                team.append_opponent(second_team)
                if team_is_winner(first_game, second_game):
                    team.add_win()


def sort_teams(teams):
    teams_dict = defaultdict(list)
    for team in teams:
        teams_dict[team.wins].append(team)
    for key in teams_dict.keys():
        teams_dict[key] = sorted(teams_dict[key], key=lambda x: x.name, reverse=False)
    return teams_dict


def print_teams(teams):
    flatten = itertools.chain.from_iterable
    sorted_teams_by_wins = sorted(teams, key=lambda x: x.wins, reverse=True)
    teams_dict = sort_teams(sorted_teams_by_wins)
    for team in flatten(teams_dict.values()):
        print(team)

