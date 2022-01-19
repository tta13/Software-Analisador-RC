import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { MatchesData } from './matches-data';

@Injectable({
  providedIn: 'root'
})
export class MatchesService {

  constructor(private http: HttpClient) { }

  getMatches(): Observable<MatchesData> {
    return this.http.get<MatchesData>('http://localhost:3000/matches');
  }
}
