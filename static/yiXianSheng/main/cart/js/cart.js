$(function () {
    // 添加购物车
    $(".plus").click(function () {
        var $button = $(this);
        var goodsid=$button.parent().attr('goodsid');

        $.get(
            '/cart/marketPlus/',
            {'goodsid':goodsid},
            function (data) {
                var goodsnum=data.goodsnums;
                $button.prev().html(goodsnum);
                var total=data.payAll;
                $("#total").html(total);
            }
        )
    })

    // 减少购物车数
    $(".reduce").click(function () {
        var $button = $(this);
        var goodsid=$button.parent().attr('goodsid');

        $.get(
            '/cart/marketReduce/',
            {'goodsid':goodsid},
            function (data) {
                var goodsnum=data.goodsnums;
                $button.next().html(goodsnum);
                var total=data.payAll;
                $("#total").html(total);
            }
        )
    })

    // 购物车增加数量
    $(".btnPlus").click(function () {
        var $btnPlus = $(this);
        var goodsid=$btnPlus.parent().attr('goodsid');

        $.get(
            '/cart/marketPlus/',
            {'goodsid':goodsid},
            function (data) {
                var goodsnum=data.goodsnums;
                $btnPlus.prev().html(goodsnum);
                var total=data.payAll;
                $("#total").html(total);
            }
        )
    })

    // 购物车减少数量
    $(".btnReduce").click(function () {
        var $btnReduce = $(this);
        var goodsid=$btnReduce.parent().attr('goodsid');

        $.get(
            '/cart/marketReduce/',
            {'goodsid':goodsid},
            function (data) {
                var goodsnum=data.goodsnums;
                var total=data.payAll;
                $("#total").html(total);
                if(goodsnum){
                    $btnReduce.next().html(goodsnum);
                }else {
                    $btnReduce.next().html(goodsnum);
                    console.log('不买就不要点我，哼');
                    $btnReduce.parent().parent().parent().css('display','none');
                }

            }
        )
    })

    // 购物车勾选商品--单选
    $(".chooseOne").click(function () {
        var $chooseOne = $(this);

        var cartid = $chooseOne.attr('cartid');
        $.get(
            '/cart/changeStatus',
            {'cartid':cartid},
            function (data) {
                var total=data.payAll;
                $("#total").html(total);
                var chooseList=[];
                if(data.choose){
                    $chooseOne.find('span').html('√');
                    $(".chooseOne").each(function () {
                        var id=$(this).attr('cartid');

                        if($(this).find('span').html()){
                            console.log('你居然有√');

                        }else {
                            chooseList.push(id);
                            $(".chooseAll").find('span').html('');
                        }
                    })
                    if(chooseList.length){
                        $(".chooseAll").find('span').html('');
                    }else {
                        $(".chooseAll").find('span').html('√');
                    }

                }else {
                    $chooseOne.find('span').html('');
                    $(".chooseAll").find('span').html('');
                }
            }
        )
    })

    // 购物车是否全选
    $(".chooseAll").click(function () {
        var $chooseAll = $(this);
        var mark=$chooseAll.find('span').html();
        $.get(
            '/cart/changeAll/',
            {'mark':mark},
            function (data) {
                var total=data.payAll;
                $("#total").html(total);
                $chooseAll.find('span').html(data.mark);
                $(".chooseOne").each(function () {
                    $(this).find('span').html(data.mark);
                })
            }
        )

    })

    // 下单
    $("#toOrder").click(function () {
        $.get(
            '/order/toOrder/',
            function (data) {
                var status=data.status
                if(status == 200){
                    window.location.href='/order/orderWeb/?ordernum='+data.ordernum+'&totalPay='+data.totalPay
                }else if(status==201){
                    window.location.href='/yxshome/cart/'
                }else {
                    window.location.href='/user/login/'
                }
            }
        )
    })

})