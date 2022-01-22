export class MatchData {
    gameResult: GameResult;
    leftTeam: TeamData;
    rightTeam: TeamData;

    constructor(){
        this.gameResult = new GameResult();
        this.leftTeam = new TeamData();
        this.rightTeam = new TeamData();
    }
}

export class GameResult{
    leftScore: number; rightScore: number;
}

export class TeamData{
    teamName: string;
    shots: number;
    onTargetShots: number;
    shotAccuracy: number;
    goals: number;
    completedPasses: number;
    wrongPasses: number;
    passAccuracy: number;
    interceptions: number;
    possession: number;
    playerDistances: number[][];
    averageDistance10: number;
    playerStamina: number;
    averageStamina10: number;
    averageStaminaPerDistance10: number;
    staminaPerDistance10: number[][];
}
