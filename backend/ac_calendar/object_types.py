from graphene_django import DjangoObjectType
from .models import Category, Work


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('name', 'order', 'id', 'works')

    def resolve_works(self, info):
        return self.works.order_by('is_ended', 'next_episode_date',)


class WorkType(DjangoObjectType):
    class Meta:
        model = Work
        fields = ('name', 'next_episode_date', 'next_episode', 'notes', 'is_ended', 'period')
