import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { UploadComponent } from './upload/upload.component';
import { MatchesComponent } from './matches/matches.component';
import { MatchTileTemplateComponent } from './matches/match-tile-template/match-tile-template.component';


@NgModule({
  declarations: [
    AppComponent,
    UploadComponent,
    MatchesComponent,
    MatchTileTemplateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
