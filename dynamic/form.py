from django import forms
from .models import Dynamic


class DynamicCreateForm(forms.ModelForm):
    text = forms.Textarea()

    class Meta:
        model = Dynamic
        fields = ('owner', 'text', 'type')
