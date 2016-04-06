/**
 * Created by vitold on 28.03.16.
 */
var current_page = 0;
/* function to load posts
* @page: offset for pages
* */
function load_posts(page){
    var url = $("#posts").data('url');
    var data ={};
    data.page = page;
    $.get(url, data, function(data){
        $("#posts").append(data);
    })
}

$(document).ready(function(){
    /* initial loading*/
    load_posts(current_page);
});

$(window).scroll(function(){
/* scroll listener*/
		if ($(document).height() - $(window).height() <= $(window).scrollTop()) {
            current_page += 2;
            console.log(current_page);
            load_posts(current_page);
}});

