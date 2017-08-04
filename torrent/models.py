from django.db import models
# Create your models here.
from django.utils import timezone
class TorrentData(models.Model):
    name= models.TextField()
    infohash=models.CharField(max_length=40)
    pub_date=models.DateTimeField('修改时间', auto_now=True)
    hot1=models.IntegerField(default=0)
    hot2=models.IntegerField(default=0)