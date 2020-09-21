from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from Cart.models import YxsCart
from Cart.views import pay_carts
from Home.models import Wheel, YxsNav, YxsMustBuy, MainShow, YxsFoodType, YxsGoods

# Create your views here.
from User.models import Users


def home(request):
    wheels = Wheel.objects.all()
    navs = YxsNav.objects.all()
    mustBuy = YxsMustBuy.objects.all()
    mainShows = MainShow.objects.all()
    context = {
        'wheels': wheels,
        'navs': navs,
        'mustBuy': mustBuy,
        'mainShows': mainShows
    }
    return render(request, 'yiXianSheng/main/home/home.html', context=context)


def cart(request):
    u_id = request.session.get('uid')
    if u_id:
        carts=YxsCart.objects.filter(u_id=u_id).filter(goods_num__gt=0)
    # 全选按钮
    #     if carts.filter(is_choose=False).exists():
    #         allChoose=False
    #     else:
    #         allChoose=True
    # 总价
        total=pay_carts(u_id)
        # total=0
        cart_goods_list=[]
        for cart in carts:
            g_id=cart.g_id
            goods = YxsGoods.objects.get(pk=g_id)
            cart_goods=[cart,goods]
            cart_goods_list.append(cart_goods)

            # if cart.is_choose:
            #     total += cart.goods_num * goods.price

        # total=float('%.3f' % total)
        useranme=Users.objects.get(pk=u_id).u_name
        context={
            "cart_goods_list":cart_goods_list,
            "useranme":useranme,
            'allChoose':not carts.filter(is_choose=False).exists(),
            'total':total
        }
        return render(request, 'yiXianSheng/main/cart/cart.html',context=context)
    else:
        return redirect(reverse('user:login'))


def market(request):
    foodTypes = YxsFoodType.objects.all()
    typeid = request.GET.get('typeid', '104749')
    try:
        goods = YxsGoods.objects.filter(categoryid=typeid).all()
        if not goods:
            typeid = '104749'
            goods = YxsGoods.objects.filter(categoryid=typeid).all()
    except Exception:
        typeid = '104749'
        goods = YxsGoods.objects.filter(categoryid=typeid).all()
    try:
        foodType = foodTypes.filter(typeid=typeid)[0]
    except Exception:
        foodType = foodTypes.filter(typeid='104749')[0]
    names = foodType.childtypenames.split("#")
    foodType_names_list = []
    for name in names:
        foodType_names_list.append(name.split(":"))
    sort_list = [
        {'name': '综合排序', 'sid': '0'},
        {'name': '单价升序', 'sid': '1'},
        {'name': '单价降序', 'sid': '2'},
        {'name': '销量升序', 'sid': '3'},
        {'name': '销量降序', 'sid': '4'},
    ]
    childcid = request.GET.get('childcid', '0')
    sid = request.GET.get('sid', '0')
    if childcid.isdigit():
        if childcid == '0':
            goods_c = goods
        else:
            goods_c = goods.filter(childcid=childcid).all()
            if not goods_c:
                childcid = '0'
                goods_c = goods
        if sid == '0':
            pass
        elif sid == '1':
            goods = goods_c.order_by('price')
        elif sid == '2':
            goods = goods_c.order_by('-price')
        elif sid == '3':
            goods = goods_c.order_by('productnum')
        elif sid == '4':
            goods = goods_c.order_by('-productnum')
        else:
            pass
    else:
        childcid = '0'
        if sid == '0':
            pass
        elif sid == '1':
            goods = goods.order_by('price')
        elif sid == '2':
            goods = goods.order_by('-price')
        elif sid == '3':
            goods = goods.order_by('productnum')
        elif sid == '4':
            goods = goods.order_by('-productnum')
        else:
            pass
    context = {
        'foodTypes': foodTypes,
        'goods': goods,
        'typeid': typeid,
        'foodType_names_list': foodType_names_list,
        'childcid': childcid,
        'sort_list': sort_list,
        'sid': sid
    }
    return render(request, 'yiXianSheng/main/market/market.html', context=context)


def mine(request):
    uid = request.session.get('uid')
    if uid:
        myuser = Users.objects.get(pk=uid)
        return render(request, 'yiXianSheng/main/mine/mine.html', {'myuser': myuser})
    else:
        return render(request, 'yiXianSheng/main/mine/mine.html')
