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


export type ErrorType = {
   __typename?: 'ErrorType';
  field: Scalars['String'];
  messages: Array<Scalars['String']>;
};

export type Mutation = {
   __typename?: 'Mutation';
  workMutation?: Maybe<WorkMutationPayload>;
};


export type MutationWorkMutationArgs = {
  input: WorkMutationInput;
};

export type Query = {
   __typename?: 'Query';
  categories?: Maybe<Array<Maybe<CategoryType>>>;
};

export type WorkMutationInput = {
  category: Scalars['ID'];
  name: Scalars['String'];
  nextEpisodeDate: Scalars['Date'];
  nextEpisode: Scalars['Int'];
  notes: Scalars['String'];
  period: Scalars['String'];
  isEnded?: Maybe<Scalars['Boolean']>;
  id?: Maybe<Scalars['ID']>;
  clientMutationId?: Maybe<Scalars['String']>;
};

export type WorkMutationPayload = {
   __typename?: 'WorkMutationPayload';
  work?: Maybe<WorkType>;
  errors?: Maybe<Array<Maybe<ErrorType>>>;
  clientMutationId?: Maybe<Scalars['String']>;
};

export enum WorkPeriod {
  Weekly = 'WEEKLY',
  Monthly = 'MONTHLY'
}

export type WorkType = {
   __typename?: 'WorkType';
  name: Scalars['String'];
  nextEpisodeDate?: Maybe<Scalars['Date']>;
  nextEpisode: Scalars['Int'];
  period?: Maybe<WorkPeriod>;
  notes: Scalars['String'];
  isEnded: Scalars['Boolean'];
};


