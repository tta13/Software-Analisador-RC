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
}
