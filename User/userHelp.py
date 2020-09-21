from hashlib import md5, sha256

from django.core.mail import send_mail
from django.template import loader


def makeEncryption(psd, salt):
    has = md5()
    has.update(salt.encode(encoding='utf8'))
    newsalt = has.hexdigest()

    has.update(psd.encode(encoding='utf8'))
    psd = has.hexdigest()

    sha = sha256(newsalt.encode('utf8'))
    sha.update(psd.encode('utf8'))

    newPsd = sha.hexdigest()+newsalt
    return newPsd


def checkPsd(new_psd, old_psd,username):
    old=old_psd[0:64]

    has = md5()
    has.update(username.encode(encoding='utf8'))
    newsalt = has.hexdigest()

    has.update(new_psd.encode(encoding='utf8'))
    psd1 = has.hexdigest()


    sha=sha256(newsalt.encode('utf8'))
    sha.update(psd1.encode('utf8'))
    new=sha.hexdigest()
    print(new)

    return new == old


def sendemail(username,email,token):
    template=loader.get_template('yiXianSheng/user/email.html')
    context={
        'name':username,
        'url':f'http://49.234.126.210:8000/user/sende_mail/?token={token}'
    }
    content=template.render(context)

    html_message = content
    subject='邮件发送测试'
    from_email='13788934153@163.com'
    recipient_list=[email]

    send_mail(subject=subject,message='',from_email=from_email,recipient_list=recipient_list,html_message=html_message)