import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class MatchStatsService {

  constructor(private http: HttpClient) { }

  getMatchStats(id: string): Observable<string>{
    return this.http.get<string>('http://localhost:3000/matches/' + id);
  }
}
