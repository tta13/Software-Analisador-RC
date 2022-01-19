import sys
import os
import argparse
import json
from Game import *
from Parser import *
from Analyzer import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rcg", help="RCG file path", metavar='<RCG log file>',
                        required=True, dest='rcg')
    parser.add_argument("--rcl", help="RCL file path", metavar='<RCL log file>',
                        required=True, dest='rcl')
    parser.add_argument(
        "--output", help="Output saving path.", metavar='<Output file path>', dest='output')
    parser.add_argument('--version', action='version', version='1.0.1')
    args = parser.parse_args()
    if args.output is None:
        args.output = args.rcg.split('.rcg')[0] + ".log.json"
        print(args.output)
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
    rcg_path = args.rcg
    rcl_path = args.rcl
    save_path = args.output
    parser = Parser(rcg_path, rcl_path)
    game = Game(parser)
    analyzer = Analyzer(game)
    analyzer.analyze()
    write_to_file(save_path, analyzer)


if __name__ == '__main__':
    main()
