$(function () {
    $('#tologin').click(function () {
        window.location.href='/user/login/';
    })

    $("#regis").click(function () {
        window.open('/user/register/','_self')
    })
})