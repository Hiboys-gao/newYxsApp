from django.db import models


# Create your models here.

class YxsCart(models.Model):
    u_id = models.IntegerField()
    g_id = models.IntegerField()
    goods_num = models.IntegerField()
    is_choose = models.BooleanField(default=True)

    class Meta:
        db_table = 'yxscart'
