import { Component, Input, OnInit } from '@angular/core';
import { MatchTileTemplateService } from './match-tile-template.service';

@Component({
  selector: 'app-match-tile-template',
  templateUrl: './match-tile-template.component.html',
  styleUrls: ['./match-tile-template.component.css']
})
export class MatchTileTemplateComponent implements OnInit {

  @Input() matchId: string;

  matchResume: string = '';

  constructor(private matchService: MatchTileTemplateService) { }

  ngOnInit(): void {
    this.matchResume = this.matchService.getResume(this.matchId);
  }

}
