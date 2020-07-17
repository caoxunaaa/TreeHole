from django import forms
from .models import Dynamic
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from .models import DynamicType


class DynamicCreateForm(forms.ModelForm):
    dynamic_types = DynamicType.objects.all()
    RADIO_CHOICES = ()
    for dynamic_type in dynamic_types:
        RADIO_CHOICES += ((dynamic_type.type_name, dynamic_type.type_name),)
    owner = forms.CharField(label='用户', widget=forms.HiddenInput())
    type = forms.ChoiceField(label='标签', widget=forms.RadioSelect, choices=RADIO_CHOICES)
    text = forms.CharField(label='动态', widget=CKEditorWidget(config_name='dynamic_ckeditor'))
    is_public = forms.BooleanField()

    class Meta:
        model = Dynamic
        fields = ('owner', 'text')

    def clean_owner(self):
        owner = self.cleaned_data['owner']
        if User.objects.filter(username=owner).exists():
            raise forms.ValidationError('用户名已经存在')
        return owner
