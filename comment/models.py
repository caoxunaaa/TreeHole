from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    user = models.ForeignKey(User, verbose_name='评论人', on_delete=models.CASCADE)
    text = models.TextField()

    comment_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
