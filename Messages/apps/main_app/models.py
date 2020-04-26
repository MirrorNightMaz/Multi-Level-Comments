from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Messages(models.Model):
    content = RichTextUploadingField(verbose_name='正文')
    reply_id = models.IntegerField(default=-1, verbose_name='回复')
    send_time = models.DateTimeField(auto_now_add=True, verbose_name='发表时间')

    def __str__(self):
        return "留言id：" + str(self.id)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name