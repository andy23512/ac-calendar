from graphene import ObjectType
from .queries import CategoryQuery


class Query(
    CategoryQuery,
    ObjectType
):
    pass


class Mutation(ObjectType):
    pass
