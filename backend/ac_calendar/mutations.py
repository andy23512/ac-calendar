from graphene import Field
from graphene_django.forms.mutation import DjangoModelFormMutation
from .object_types import WorkType
from .forms import WorkForm


class WorkMutation(DjangoModelFormMutation):
    work = Field(WorkType)

    class Meta:
        form_class = WorkForm
