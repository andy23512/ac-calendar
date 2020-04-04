from graphene import ObjectType, Schema
import ac_calendar.schema


class Query(
    ac_calendar.schema.Query,
    ObjectType
):
    pass


class Mutation(
    ObjectType
):
    pass


schema = Schema(query=Query)
