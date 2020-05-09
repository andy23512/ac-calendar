from datetime import timedelta
from graphene import Field, Mutation, ID
from graphene_django.forms.mutation import DjangoModelFormMutation
from .object_types import WorkType
from .forms import WorkForm
from .models import Work


class WorkMutation(DjangoModelFormMutation):
    work = Field(WorkType)

    class Meta:
        form_class = WorkForm


class NextEpisodeMutation(Mutation):
    work = Field(WorkType)

    class Arguments:
        id = ID(required=True)

    def mutate(cls, info, id):
        work = Work.objects.get(pk=id)
        if work.period == 'weekly':
            work.next_episode = work.next_episode + 1
            work.next_episode_date = work.next_episode_date + timedelta(days=7)
            work.save()
        # Notice we return an instance of this mutation
        return cls(work=work)
