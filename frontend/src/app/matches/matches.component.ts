import { Component, OnInit } from '@angular/core';
import { MatchesData } from './matches-data';
import { MatchesService } from './matches.service';

@Component({
  selector: 'app-matches',
  templateUrl: './matches.component.html',
  styleUrls: ['./matches.component.css']
})
export class MatchesComponent implements OnInit {
  matchData: MatchesData = new MatchesData();

  constructor(private matchesService: MatchesService) { }

  ngOnInit(): void {
    this.matchesService.getMatches()
      .subscribe((matches: MatchesData) => this.matchData = matches);
  }

}
