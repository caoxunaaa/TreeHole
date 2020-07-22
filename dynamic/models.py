from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Mood(models.Model):
    type_name = models.CharField(verbose_name='心情类型', max_length=10)

    def __str__(self):
        return self.type_name


class DynamicType(models.Model):
    type_name = models.CharField(verbose_name='类型名称', max_length=10, default='心情')
    mood = models.ForeignKey(Mood, verbose_name='心情类型', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['-type_name']


class Dynamic(models.Model):
    owner = models.ForeignKey(User, verbose_name='发起人', on_delete=models.CASCADE)
    text = RichTextUploadingField()
    type = models.ForeignKey(DynamicType, verbose_name='标签', on_delete=models.CASCADE, blank=True, null=True)

    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    is_public = models.BooleanField(verbose_name='是否公开', default=True)
    is_delete = models.BooleanField(verbose_name='已删除', default=False)

    def __str__(self):
        return self.text[:10]

    def get_text(self):
        return self.text[:10]

    class Meta:
        ordering = ['-update_time']
