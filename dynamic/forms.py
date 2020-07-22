from django import forms
from .models import Dynamic
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DynamicCreateForm(forms.ModelForm):
    is_public = forms.BooleanField(label='公开否')
    text = forms.CharField(label='动态', widget=CKEditorUploadingWidget(config_name='default'),
                           error_messages={'required': '评论不能为空'})

    class Meta:
        model = Dynamic
        fields = ['is_public', 'text']
