from graphene_django import DjangoObjectType
from .models import Category, Work


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('name', 'order', 'id', 'works')


class WorkType(DjangoObjectType):
    class Meta:
        model = Work
        fields = ('name', 'next_episode', 'notes',)
