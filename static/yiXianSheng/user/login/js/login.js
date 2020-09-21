$(function () {
    $('#i_code').click(function () {
        var code=document.getElementById('i_code');
        code.src='/user/checkCode/'+Math.random();
    })

    $("#log_back").click(function () {
        window.location.href='/yxshome/mine/'
    })


    $("form").submit(function () {

    // 密码加密
        var psd = $('#examplePassword').val();
        var newpsd = hex_sha1(psd)
        $('#examplePassword').val(newpsd)
        return true
    })


})
