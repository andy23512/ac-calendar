import { BrowserModule } from '@angular/platform-browser';
import { NgModule, APP_INITIALIZER } from '@angular/core';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { GraphQLModule } from './graphql.module';
import {
  HttpClientModule,
  HttpClient,
  HttpClientXsrfModule
} from '@angular/common/http';
import {
  MatToolbarModule,
  MatListModule,
  MatIconModule
} from '@angular/material';
import { CommonModule } from '@angular/common';

export function getCsrf(http: HttpClient) {
  return () => http.get('/api/csrf').toPromise();
}

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    CommonModule,
    BrowserAnimationsModule,
    GraphQLModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'ac-calendar-csrf',
      headerName: 'X-CSRFToken'
    }),
    MatToolbarModule,
    MatListModule,
    MatIconModule
  ],
  providers: [
    {
      provide: APP_INITIALIZER,
      useFactory: getCsrf,
      multi: true,
      deps: [HttpClient]
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
