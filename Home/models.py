from django.db import models


# Create your models here.

class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=32)
    trackid = models.CharField(max_length=32)

    class Meta:
        db_table = 'yxs_wheel'


class YxsNav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=32)
    trackid = models.CharField(max_length=32)

    class Meta:
        db_table = 'yxs_nav'


class YxsMustBuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=32)
    trackid = models.CharField(max_length=32)

    class Meta:
        db_table = 'yxs_mustbuy'


class MainShow(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=32)
    trackid = models.CharField(max_length=32)
    categoryid = models.CharField(max_length=32)
    brandname = models.CharField(max_length=32)

    img1 = models.CharField(max_length=150)
    childcid1 = models.CharField(max_length=32)
    productid1 = models.CharField(max_length=32)
    longname1 = models.CharField(max_length=32)
    price1 = models.CharField(max_length=32)
    marketprice1 = models.CharField(max_length=32)

    img2 = models.CharField(max_length=150)
    childcid2 = models.CharField(max_length=32)
    productid2 = models.CharField(max_length=32)
    longname2 = models.CharField(max_length=32)
    price2 = models.CharField(max_length=32)
    marketprice2 = models.CharField(max_length=32)

    img3 = models.CharField(max_length=150)
    childcid3 = models.CharField(max_length=32)
    productid3 = models.CharField(max_length=32)
    longname3 = models.CharField(max_length=32)
    price3 = models.CharField(max_length=32)
    marketprice3 = models.CharField(max_length=32)

    class Meta:
        db_table = 'yxs_mainshow'


class YxsFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=32)
    childtypenames = models.CharField(max_length=128)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'yxs_foodtype'


class YxsGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=128)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=128)

    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()

    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=64)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'yxs_goods'
