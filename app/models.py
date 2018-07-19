from django.db import models

# Create your models here.
from django.db import models


class Books(models.Model):
    # to_user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='attitude_receive')      # 接收者
    # from_user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='attitude_send')       # 发送者
    title = models.CharField(max_length=128)                                       # 书名


class Segment(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name='s_book')
    text = models.CharField(max_length=128)


class Chapter(models.Model):
    book_id = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name='c_book')
    segment_id = models.ForeignKey(Books, on_delete=models.DO_NOTHING, related_name='c_segment')
    text = models.CharField(max_length=128)

