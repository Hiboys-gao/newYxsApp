from django.db import models

# Create your models here.

class MyOrder(models.Model):
    m_uid = models.IntegerField()
    m_gid = models.IntegerField()
    m_goods_num = models.IntegerField()
    m_time=models.DateTimeField(auto_now_add=True)
    m_order_num=models.CharField(max_length=32)
    m_ispay=models.BooleanField(default=False)

    class Meta:
        db_table='myorder'