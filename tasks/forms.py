from django import forms
from .models import Task, mSequencia

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description')

class SeqForm(forms.ModelForm):
    class Meta:
        model = mSequencia
        fields = ('titulo', 'fasta', 'tipo')