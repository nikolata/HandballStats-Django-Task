
from collections import defaultdict
import itertools
from .models import Team
from django.utils import timezone

def team_is_winner(left_score, right_score):
    points_left_team = int(left_score.split(":")[0]) + int(right_score.split(":")[1])
    points_right_team = int(left_score.split(":")[1]) + int(right_score.split(":")[0])
    if points_left_team > points_right_team:
        return True
    if points_right_team == points_left_team and int(right_score.split(":")[1]) > int(left_score.split(":")[1]):
        return True
    return False


def store_info_from_input(first_team, second_team, first_game, second_game, viewed_teams, teams):
    if first_team not in [str(elem[0]) for elem in list(Team.objects.all().values_list('name'))]:
        viewed_teams.append(first_team)
        temp = Team(name=first_team, wins=0, opponents="")
        temp.opponents = second_team
        temp.added = timezone.now()
        if team_is_winner(first_game, second_game):
            temp.wins += 1
            temp.last_win = timezone.now()
        temp.save()
    else:
        temp = Team.objects.get(name=first_team)
        if temp.opponents.count(second_team) == 0:
            temp.opponents = temp.opponents + " " + second_team
            temp.last_match = timezone.now()
        if team_is_winner(first_game, second_game):
            temp.wins += 1
            temp.last_win = timezone.now()
        temp_opponents_list = temp.opponents.split(" ")
        temp.opponents = ", ".join(sorted(temp_opponents_list))
        temp.save()


def sort_teams(teams):
    teams_dict = defaultdict(list)
    for team in teams:
        teams_dict[team.wins].append(team)
    for key in teams_dict.keys():
        teams_dict[key] = sorted(teams_dict[key], key=lambda x: x.name, reverse=False)
    return teams_dict


def order_teams(teams):
    flatten = itertools.chain.from_iterable
    sorted_teams_by_wins = sorted(teams, key=lambda x: x.wins, reverse=True)
    teams_dict = sort_teams(sorted_teams_by_wins)
    return list(flatten(teams_dict.values()))


