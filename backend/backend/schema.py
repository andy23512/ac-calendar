from graphene import ObjectType, Schema
import ac_calendar.schema


class Query(
    ac_calendar.schema.Query,
    ObjectType
):
    pass


class Mutation(
    ac_calendar.schema.Mutation,
    ObjectType
):
    pass


schema = Schema(query=Query, mutation=Mutation)
