import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MatchTileTemplateService {

  constructor() { }

  getResume(matchId: string): string {
    const split1 = matchId.split('.')[0].split('-');
    const leftTeamInfo = split1[1];
    const rightTeamInfo = split1[3];
    const splitLeftTeam = leftTeamInfo.split('_');
    const splitRightTeam = rightTeamInfo.split('_');

    return splitLeftTeam[0] + ' ' + splitLeftTeam[1] + 'x' + splitRightTeam[1] + ' ' + splitRightTeam[0];    
  }
}
