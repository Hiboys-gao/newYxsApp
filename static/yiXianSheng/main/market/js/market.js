$(function () {
    $('#goods_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $("#div_goods").toggle()
    })
    $('#all_sort').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $('#div_sort').toggle()

    })
})