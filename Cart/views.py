from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from Cart.models import YxsCart


# 添加
from Home.models import YxsGoods


def marketPlus(request):
    g_id = int(request.GET.get('goodsid'))
    u_id = int(request.session.get('uid'))
    carts = YxsCart.objects.filter(u_id=u_id).filter(g_id=g_id)
    if carts.exists():
        cart = carts.first()
        goodsnum = cart.goods_num + 1
        cart.goods_num = goodsnum
    else:
        goodsnum = 1
        cart = YxsCart(
            u_id=u_id,
            g_id=g_id,
            goods_num=goodsnum,
        )
    cart.save()
    payAll=pay_carts(u_id)

    data = {
        'status': 200,
        'goodsnums': goodsnum,
        'payAll':payAll
    }
    return JsonResponse(data)

# 减少
def marketReduce(request):
    u_id = int(request.session.get('uid'))
    g_id = int(request.GET.get('goodsid'))
    carts = YxsCart.objects.filter(u_id=u_id).filter(g_id=g_id)
    if carts.exists():
        cart = carts.first()
        goodsnum = cart.goods_num
        if goodsnum >= 1:
            goodsnum -= 1
            cart.goods_num = goodsnum
            cart.save()
        else:
            goodsnum = 0
    else:
        goodsnum = 0

    payAll = pay_carts(u_id)
    data = {
        'status': 200,
        'goodsnums': goodsnum,
        'payAll':payAll
    }
    return JsonResponse(data)

# 购物车单选
def changeStatus(request):
    u_id = int(request.session.get('uid'))
    cartid=request.GET.get('cartid')
    cart=YxsCart.objects.get(pk=cartid)
    cart.is_choose = not cart.is_choose
    cart.save()
    payAll = pay_carts(u_id)
    data={
        'status':200,
        'choose':cart.is_choose,
        'payAll':payAll
    }
    return JsonResponse(data)

# 购物车全选
def changeAll(request):
    mark=request.GET.get('mark')
    uid=request.session.get('uid')
    carts=YxsCart.objects.filter(u_id=uid)
    if mark:
        for cart in  carts.filter(is_choose=True).all():
            cart.is_choose = not cart.is_choose
            cart.save()
        mark = ''
    else:
        for cart in carts.filter(is_choose=False).all():
            cart.is_choose = not cart.is_choose
            cart.save()
        mark = '√'

    payAll = pay_carts(uid)
    data={
        'status':200,
        'mark':mark,
        'payAll':payAll
    }
    return JsonResponse(data)

def pay_carts(u_id):
    pay_carts = YxsCart.objects.filter(u_id=u_id).filter(is_choose=1)
    payAll=0
    if  pay_carts:
        for cart in pay_carts:
            goods=YxsGoods.objects.get(pk=cart.g_id)
            payAll += goods.price*cart.goods_num
    else:
        pass

    payAll=float('%.3f' % payAll)
    return payAll