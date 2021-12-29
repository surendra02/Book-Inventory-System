from django.db import models
import datetime
from django.db.models.signals import post_save,pre_save

# Create your models here.
class Books(models.Model):
    bname = models.CharField(max_length=40)
    b_title = models.CharField(max_length=150)
    b_author = models.CharField(max_length=40)
    publish_date = models.DateField(default=datetime.date.today())
    total_quantity = models.BigIntegerField(max_length=5)
    aval_quantity = models.BigIntegerField(max_length=5,null=True,blank=True)

    def __str__(self):
        return self.bname


# def userReciever(sender,instance,**kwargs):
#     if instance.aval_quantity is None:
#         instance.aval_quantity=instance.total_quantity
# pre_save.connect(userReciever,sender=Books)


