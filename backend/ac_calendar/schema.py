from graphene import ObjectType
from .queries import CategoryQuery
from .mutations import WorkMutation, NextEpisodeMutation


class Query(
    CategoryQuery,
    ObjectType
):
    pass


class Mutation(ObjectType):
    work_mutation = WorkMutation.Field()
    next_episode_mutation = NextEpisodeMutation.Field()
