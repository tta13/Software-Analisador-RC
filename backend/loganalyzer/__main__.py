import sys
import os
import argparse
import json
from .Game import *
from .Parser import *
from .Analyzer import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="Input file path", metavar='<log file without .rcl or .rcg >',
                        required=True, dest='path')
    parser.add_argument(
        "--save_path", help="Output saving path.", metavar='<save_path>', dest='save_path')
    parser.add_argument("--heatmap", help="Show Heatmap of Selected Side", metavar='TEAM_SIDE',
                        dest='heat_map')
    parser.add_argument('--version', action='version', version='1.0.1')
    args = parser.parse_args()
    if args.save_path is None:
        args.save_path = args.path+".log.json"
    return args


def write_to_file(save_path, analyzer):
    # left TEAM
    left_team_data = {
        "teamName": analyzer.game.left_team.name,
        "shots": analyzer.off_target_shoot_l + analyzer.on_target_shoot_l,
        "onTargetShots": analyzer.on_target_shoot_l,
        "shotAccuracy": analyzer.shoot_accuracy_l,
        "goals": analyzer.game.left_goal,
        "completedPasses": analyzer.pass_l,
        "wrongPasses": analyzer.intercept_r,
        "passAccuracy": analyzer.pass_accuracy_l,
        "interceptions": analyzer.intercept_l,
        "possession": analyzer.possession_l,
        "playersDistances": analyzer.team_moved_distance_l,
        "averageDistance10": analyzer.average_distance_10p_l,
        "playersStamina": analyzer.used_stamina_agents_l,
        "averageStamina10": analyzer.average_stamina_10p_l,
        "averageStaminaPerDistance10": analyzer.av_st_per_dist_10p_l,
        "staminaPerDistance": analyzer.used_per_distance_l
    }

    # right TEAM
    right_team_data = {
        "teamName": analyzer.game.right_team.name,
        "shots": analyzer.off_target_shoot_r + analyzer.on_target_shoot_r,
        "onTargetShots": analyzer.on_target_shoot_r,
        "shotAccuracy": analyzer.shoot_accuracy_r,
        "goals": analyzer.game.right_goal,
        "completedPasses": analyzer.pass_r,
        "wrongPasses": analyzer.intercept_l,
        "passAccuracy": analyzer.pass_accuracy_r,
        "interceptions": analyzer.intercept_r,
        "possession": analyzer.possession_r,
        "playersDistances": analyzer.team_moved_distance_r,
        "averageDistance10": analyzer.average_distance_10p_r,
        "playersStamina": analyzer.used_stamina_agents_r,
        "averageStamina10": analyzer.average_stamina_10p_r,
        "averageStaminaPerDistance10": analyzer.av_st_per_dist_10p_r,
        "staminaPerDistance": analyzer.used_per_distance_r
    }

    data = {
        "gameResult": {analyzer.game.left_team.name: analyzer.game.left_goal,
                       analyzer.game.right_team.name: analyzer.game.right_goal},
        "leftTeam": left_team_data,
        "rightTeam": right_team_data,
    }

    with open(save_path, 'w') as outfile:
        json.dump(data, outfile, indent=1)


def main():
    args = parse_args()
    path = args.path
    save_path = args.save_path
    parser = Parser(path)
    game = Game(parser)
    analyzer = Analyzer(game)
    analyzer.analyze()
    write_to_file(save_path, analyzer)

    # Drawing Heatmap of the game

    if args.heat_map is not None:
        analyzer.draw_heatmap(right_team=True, left_team=True)

main()
