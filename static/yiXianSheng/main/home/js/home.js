$(function () {
    topwheel();
    swiperMenu();
    mainInfo();
})

function topwheel() {
    var topwheel = new Swiper('#topSwiper',
        {
            // observer: true,
            // observeParents: true,
            loop: true,
            autoplay: 3000,
            pagination: '.swiper-pagination',
            autoplayDisableOnInteraction: false,

        })
}

function swiperMenu() {
    var swiperMenu=new Swiper('#swiperMenu',
        {
            slidesPerView :3,
        })
}

function mainInfo() {
    var mainInfo = new Swiper('#mainInfo',
        {
            // slidesPerView :1,
        })
}