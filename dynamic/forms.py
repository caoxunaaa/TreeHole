from django import forms
from .models import Dynamic
from ckeditor.widgets import CKEditorWidget


class DynamicCreateForm(forms.ModelForm):
    is_public = forms.BooleanField(label='公开否')
    text = forms.CharField(label='动态', widget=CKEditorWidget(config_name='default'),
                           error_messages={'required': '评论不能为空'})

    class Meta:
        model = Dynamic
        fields = ['is_public', 'text']
