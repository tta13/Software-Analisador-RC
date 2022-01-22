import { Component, OnInit } from '@angular/core';
import { MatchData } from './match-data';
import { ActivatedRoute } from '@angular/router'
import { MatchStatsService } from './match-stats.service';

@Component({
  selector: 'app-match-stats',
  templateUrl: './match-stats.component.html',
  styleUrls: ['./match-stats.component.css']
})
export class MatchStatsComponent implements OnInit {

  matchData: MatchData = new MatchData;

  constructor(private statsService: MatchStatsService, private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.route.paramMap
    .subscribe(params => {

      this.statsService.getMatchStats(params.get('id') as string)
        .subscribe((data) => {
          this.matchData = JSON.parse(data);
        });
    });
  }

}
