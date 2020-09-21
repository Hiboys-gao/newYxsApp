import datetime

from alipay import AliPay, AliPayConfig
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from Cart.models import YxsCart
from Cart.views import pay_carts
from Home.models import YxsGoods
from Order.models import MyOrder
from yixianshengApp.settings import PRIVATE_KEY, PUBLIC_KEY


def toOrder(request):
    uid = request.session.get('uid')
    if uid:
        carts = YxsCart.objects.filter(u_id=uid).filter(is_choose=True).filter(goods_num__gt=0)
        if carts.exists():
            now = datetime.datetime.now()
            ordernum = '%04d%02d%02d%02d%02d%02d%d' % (
                now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
            # order_liset = []
            totalPay = pay_carts(uid)
            for cart in carts:
                goodsid = cart.g_id
                goods_num = cart.goods_num
                order = MyOrder(m_uid=uid, m_gid=goodsid, m_goods_num=goods_num, m_time=now, m_order_num=ordernum)
                order.save()
                cart.goods_num = 0
                cart.save()

                # goods = YxsGoods.objects.get(pk=goodsid)
                # order_liset.append([goods, goods_num])
            data = {
                # 'order_liset': order_liset,
                # 'totalPay': pay_carts(uid),
                'ordernum': ordernum,
                'totalPay': totalPay,
                'status': 200
            }
            return JsonResponse(data=data)
        else:
            data = {'status': 201}
            return JsonResponse(data=data)
    else:
        data = {'status': 204}
        return JsonResponse(data=data)


def payOrder(request):
    totalPay = request.GET.get('totalPay')
    print(totalPay)
    alipay = AliPay(
        appid="2016093000627735",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=PRIVATE_KEY,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=PUBLIC_KEY,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug=False,  # 默认False
        config=AliPayConfig(timeout=15)  # 可选, 请求超时时间
    )

    subject = "测试订单"
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no="110",
        total_amount=totalPay,
        subject=subject,
        return_url="http://www.1000phone.com",
        notify_url="http://www.1000phone.com"  # 可选, 不填则使用默认notify url
    )

    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)


def orderWeb(request):
    uid = request.session.get('uid')
    ordernum = request.GET.get('ordernum')
    totalPay = request.GET.get('totalPay')
    if uid and ordernum:
        orders = MyOrder.objects.filter(m_order_num=ordernum)
        if orders:

            order_liset = []
            for order in orders:
                goodsnum = order.m_goods_num
                gid = order.m_gid
                goods = YxsGoods.objects.get(pk=gid)
                order_liset.append([goods, goodsnum])
            context = {
                'order_liset': order_liset,
                'totalPay': totalPay,
            }
            return render(request, 'yiXianSheng/pay/order.html', context=context)
        else:
            return redirect(reverse('yxshome:cart'))
    else:
        return redirect(reverse('user:login'))
