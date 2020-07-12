from django.db import models
from django.contrib.auth.models import User


class DynamicType(models.Model):
    type_name = models.CharField(verbose_name='类型名称', max_length=10)

    def __str__(self):
        return self.type_name


class Dynamic(models.Model):
    owner = models.ForeignKey(User, verbose_name='发起人', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='正文')
    type = models.ForeignKey(DynamicType, verbose_name='标签', on_delete=models.CASCADE)

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
