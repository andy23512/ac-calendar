import { Injectable } from '@angular/core';
import { Apollo } from 'apollo-angular';
import { CategoryType } from '@frontend/interface';
import gql from 'graphql-tag';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  constructor(private apollo: Apollo) {}

  public watchQueryAllData() {
    return this.apollo.watchQuery<{
      categories: CategoryType[];
    }>({
      query: gql`
        query Categories {
          categories {
            id
            name
            order
            works {
              name
              nextEpisode
              notes
            }
          }
        }
      `
    });
  }
}
