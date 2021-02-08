/**
* headerScroll.js
**/
$(function(){
    $(window).on('scroll',function(){
        var scroll_top=$(this).scrollTop();

        if(scroll_top>=580){
            $('header').css({'background-color':'white',
                            'border-bottom':'1px solid black'});
            $('#whiteLogo').attr('src','static/image/waug_logo.png');
            $('#topMenuBox').css({'color':'#ff69b4',
                                'font-weight':'bold'});
        };
        if(scroll_top<580){
            $('header').css({'background-color':'transparent',
                            'border':'none'});
            $('#whiteLogo').attr('src','static/image/waug_logo.svg');
            $('#topMenuBox').css('color','white');
        };

    });
});