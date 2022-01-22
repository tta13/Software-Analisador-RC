import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { UploadComponent } from './upload/upload.component';
import { MatchesComponent } from './matches/matches.component';
import { MatchStatsComponent } from './match-stats/match-stats.component';

const routes: Routes = [
  {path: 'upload', component: UploadComponent},
  {path: 'matches', component: MatchesComponent},
  {path: 'matches/:id', component: MatchStatsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
