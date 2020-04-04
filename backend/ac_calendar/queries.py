from graphene import ObjectType, List
from .models import Category
from .object_types import CategoryType


class CategoryQuery(ObjectType):
    categories = List(CategoryType)

    def resolve_categories(parent, info):
        return Category.objects.all().order_by('order')

