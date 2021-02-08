/**
* slideshow.js
**/

$(function(){
    $('#Button img:eq(1)').on('click',function(){
        $('#Button img:eq(1)').attr('src','static/image/controlButton2.png');
        $('#Button img:eq(0)').attr('src','static/image/controlButton1.png');
        $('#MainPhoto').animate({'left':-1900},0);
        $('#TBox span').text('전국 스키장 어디든 할인돼요.');
        $('#Appendix').text('리프트권부터 장비 렌탈까지');
    });
    $('#Button img:eq(0)').on('click',function(){
        $('#Button img:eq(0)').attr('src','static/image/controlButton2.png');
        $('#Button img:eq(1)').attr('src','static/image/controlButton1.png');
        $('#MainPhoto').animate({'left':0},0);
        $('#TBox span').text('낭만 가득한 겨울 캠핑을 만나보세요.');
        $('#Appendix').text('감성 차박 패키지');
    });
});