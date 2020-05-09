from django.forms import ModelForm
from .models import Work


class WorkForm(ModelForm):
    class Meta:
        model = Work
        fields = ('category', 'name', 'next_episode_date', 'next_episode', 'notes', 'period', 'is_ended')
