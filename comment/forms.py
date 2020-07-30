from django import forms
from .models import Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.contenttypes.models import ContentType


class CommentCreateForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput())
    object_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['content_type', 'object_id']

    def clean(self):
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            # 从前端的到的是content_type字符,转换成ContentType类型
            self.cleaned_data['content_type'] = ContentType.objects.get(model=content_type)
            # 得到模型model_class
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)
            self.cleaned_data['content_object'] = model_obj
        except:
            print('no exists')
        return self.cleaned_data
