import { Component, OnInit } from '@angular/core';
import { MatchData } from './match-data';
import { ActivatedRoute } from '@angular/router'
import { MatchStatsService } from './match-stats.service';
import { BehaviorSubject, Observable } from "rxjs";

@Component({
  selector: 'app-match-stats',
  templateUrl: './match-stats.component.html',
  styleUrls: ['./match-stats.component.css']
})
export class MatchStatsComponent implements OnInit {

  matchData: MatchData = new MatchData;
  loading: BehaviorSubject<boolean> = new BehaviorSubject(false as boolean)

  constructor(private statsService: MatchStatsService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.getMatchStats();
  }

  private getMatchStats() {
    this.loading.next(true);

    this.route.paramMap
      .subscribe(params => {
        this.statsService.getMatchStats(params.get('id') as string)
          .subscribe({
            next: (data) => this.matchData = JSON.parse(data),
            complete: () => this.loading.next(false),
          });
      });
  }

  isLoading(): Observable<boolean> {
    return this.loading.asObservable();
  }

  parseScorers(scorers: [number,string][]): string{
    if(scorers == null || scorers.length === 0)
      return '-'
    let scorerString: string = '';
    const scorersSize = scorers.length;
    for(var i=0; i < scorersSize; i++){
      scorerString += this.convertCycleToHumanReadable(scorers[i][0]) + ' ' + scorers[i][1];
      if((i+1) != scorersSize)
        scorerString += '\n';
    }
    return scorerString;
  }

  convertCycleToHumanReadable(cycle: number): string {
    const seconds = Math.floor(cycle / 10);
    const remainingSeconds = seconds % 60;
    const minutes: number = remainingSeconds > 30 ? Math.ceil(seconds / 60) : Math.floor(seconds / 60);
    return minutes+"\'";
  }
}
