from graphene import ObjectType
from .queries import CategoryQuery
from .mutations import WorkMutation


class Query(
    CategoryQuery,
    ObjectType
):
    pass


class Mutation(ObjectType):
    work_mutation = WorkMutation.Field()
