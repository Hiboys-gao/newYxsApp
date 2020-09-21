$(function () {
    $("#payMoney").click(function () {
        var totalPay=$(this).prev().find('span').html()
        window.location.href='/order/payOrder/?totalPay='+totalPay
    })
})