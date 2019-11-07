$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    console.log(scroll)


document.getElementById("myBody").style.marginTop  = (-100- 0.5*scroll) +"px";
    if(scroll >= 300) {
        $("#myNav").addClass("bg-danger");
    } else {
        $("#myNav").removeClass("bg-danger");
    }
});