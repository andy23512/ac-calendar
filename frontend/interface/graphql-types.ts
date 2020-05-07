// @ts-ignore: Unused variable
import gql from 'graphql-tag';
export type Maybe<T> = T | null;

/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  Date: any;
};



export type CategoryType = {
   __typename?: 'CategoryType';
  id: Scalars['ID'];
  name: Scalars['String'];
  order: Scalars['Int'];
  works: Array<WorkType>;
};


export type Query = {
   __typename?: 'Query';
  categories?: Maybe<Array<Maybe<CategoryType>>>;
};

export type WorkType = {
   __typename?: 'WorkType';
  name: Scalars['String'];
  nextEpisodeDate?: Maybe<Scalars['Date']>;
  nextEpisode: Scalars['Int'];
  notes: Scalars['String'];
};


