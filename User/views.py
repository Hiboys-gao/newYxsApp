import uuid

from django.core.cache import cache
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string, io

# Create your views here.
from django.urls import reverse

from User.models import Users
from User.userHelp import makeEncryption, checkPsd, sendemail
from yixianshengApp import settings


def checkCode(request):
    # 背景颜色
    bgcolor = (random.randrange(10, 255), random.randrange(50, 160), 255)

    # 宽高
    width = 100
    height = 50

    # 创建画板
    img = Image.new(mode='RGB', size=(width, height), color=bgcolor)

    # 创建画笔
    draw = ImageDraw.Draw(img, mode='RGB')

    for i in range(200):
        fill = (random.randrange(256), random.randrange(256), random.randrange(256))
        xy = (random.randrange(100), random.randrange(50))
        draw.point(xy=xy, fill=fill)

    # 定义字符
    text = string.digits + string.ascii_letters
    font1 = ImageFont.truetype(settings.FONT_PATH, 30)

    code = ''
    for i in range(4):
        code1 = text[random.randrange(0, len(text))]
        code += code1
        color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.text((i * 24, i * 6), code1, color1, font1)

        # 干扰线
        linecolor = (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))
        for i in range(2):
            begin = (random.randint(0, width), random.randint(0, height))
            end = (random.randint(0, width), random.randint(0, height))
            draw.line([begin, end], fill=linecolor)

    # img = img.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

    buf = io.BytesIO()
    img.save(buf, 'png')
    request.session['code'] = code

    return HttpResponse(buf.getvalue(), 'image/png')


def login(request):
    if request.method=='POST':
        code=request.POST.get('u_code')
        checkcode=request.session.get('code')
        if code.lower() == checkcode.lower():
            username=request.POST.get('name')
            user=Users.objects.filter(u_name=username)
            if user.exists():
                password=request.POST.get('password')
                old_psd=user[0].u_password
                if checkPsd(password,old_psd,username):
                    if user[0].u_active:
                        request.session['uid']=user[0].id
                        return redirect(reverse('yxshome:mine'))
                    else:
                        return render(request, 'yiXianSheng/user/login.html', {'erro': '该用户未激活账户!!!'})
                else:
                    return render(request, 'yiXianSheng/user/login.html', {'erro': '密码不正确!!!'})
            else:
                return render(request, 'yiXianSheng/user/login.html', {'erro': '用户名不存在!!!'})
        else:
            return render(request, 'yiXianSheng/user/login.html',{'erro':'验证码错误!!!'})
    else:
        return render(request, 'yiXianSheng/user/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        icon = request.FILES.get('icon')
        newPsd = makeEncryption(password, username)
        token = uuid.uuid4()
        user = Users(
            u_name=username,
            u_password=newPsd,
            u_mail=email,
            u_icon=icon,
            u_tokon=token
        )
        user.save()

        sendemail(username, email, token)

        cache.set(token, user.id, timeout=30)

        return redirect(reverse('user:login'))

    else:
        return render(request, 'yiXianSheng/user/register.html')


def checkUser(request):
    data = request.POST.get('username')
    user = Users.objects.filter(u_name=data)
    if user:
        msg = {'data': True}
    else:
        msg = {'data': False}
    return JsonResponse(msg)


def sende_mail(request):
    token = request.GET.get('token')
    uid=cache.get(token)

    if uid:
        user=Users.objects.get(pk=uid)
        user.u_active=True
        user.save()

        cache.delete(token)
        return HttpResponse('激活成功')
    else:
        return HttpResponse('邮件已过期，请重新激活')


def logout(request):
    request.session.delete()
    return render(request , 'yiXianSheng/main/mine/mine.html')