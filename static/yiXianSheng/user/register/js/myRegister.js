$(function () {
    username();
    psd1();
    psd2();
    email();
    icon();
    button();

    $("#res_back").click(function () {
        window.location.href = '/yxshome/mine/'
    });

})

var name_flag = false;
var psd1_flag = false;
var psd2_flag = false;
var mail_flag = false;
var icon_flag = false;

function username() {
    $('#span_user').html('用户名长度4--12位！');
    $('input[name=username]').blur(function () {
        var user = $(this).val().trim();
        var user_len = user.length;
        if (user_len < 4 || user_len > 12) {
            $('#span_user').html('用户名长度不合法，请重新输入！').removeClass().addClass('glyphicon glyphicon-remove').css('color', 'red');
            name_flag = false;
        } else {

            // $.post(url,[data],[callback],[dataType]])
            $.post('/user/checkUser', {'username': user}, function (msg) {
                if (msg.data) {
                    $('#span_user').html('用户名已存在，请重新输入！').removeClass().addClass('glyphicon glyphicon-remove').css('color', 'red');
                    name_flag = false;
                } else {
                    $('#span_user').html('').removeClass().addClass('glyphicon glyphicon-ok').css('color', 'green');
                    name_flag = true;
                }
            }, 'json')
        }
    })
}

function psd1() {
    $('#span_psd1').html('密码长度8--16位！只能是字母、数字！');
    $('input[name=password]').blur(function () {
        var psd1 = $(this).val().trim();
        var psd1_len = psd1.length;
        var psd_check = "^[A-Za-z0-9]+$";
        if (psd1_len < 8 || psd1_len > 16) {
            $('#span_psd1').html('密码长度需8--16位！请重新输入！').removeClass().addClass('glyphicon glyphicon-remove').css('color', 'red');
            psd1_flag = false;
        } else {
            if (psd1.match(psd_check)) {
                $('#span_psd1').html('').removeClass().addClass('glyphicon glyphicon-ok').css('color', 'green');
                psd1_flag = true;

            } else {
                $('#span_psd1').html('密码只能是字母、数字！请重新输入！').removeClass().addClass('glyphicon glyphicon-remove').css('color', 'red');
                psd1_flag = false;
            }
        }
    })
}

function psd2() {

    $('input[name=password_again]').blur(function () {
        var psd2 = $(this).val().trim();
        var psd1 = $('input[name=password]').val().trim();
        if (psd1 == psd2) {
            $('#span_psd2').html('').removeClass().addClass('glyphicon glyphicon-ok').css('color', 'green');
            psd2_flag = true;
        } else {
            $('#span_psd2').html('两次密码输入不相同，请重新输入！').removeClass().addClass('glyphicon glyphicon-remove').css('color', 'red');
            $(this).val('');
            psd2_flag = false
        }
    })
}

function email() {
    $('#span_email').html('请输入正确的邮箱地址！');
    $('input[name=email]').blur(function () {
        var email_check = "^([A-z0-9]{6,18})(\\w|\\-)+@[A-z0-9]+\\.([A-z]{2,3})$";

        var email = $(this).val().trim()
        if (email.match(email_check)) {
            $('#span_email').html('').removeClass().addClass('glyphicon glyphicon-ok').css('color', 'green');
            mail_flag = true;
        } else {
            $('#span_email').html('邮箱地址不合法，请重新输入！').removeClass().addClass('glyphicon glyphicon-remove').css('color', 'red');
            $(this).val('');
            mail_flag = false;
        }
    })
}

function icon() {
    $("input[name=icon]").blur(function () {
        var value=$(this).val();
        icon_flag = !!value;
    })
}

function button() {
    $('form').submit(function () {
        // 加密
        var psd1=$("input[name=password]").val();
        var shalpassword = hex_sha1(psd1);
        $("input[name=password]").val(shalpassword);

        return !!(name_flag & psd1_flag & psd2_flag & mail_flag & icon_flag);
    })
}


