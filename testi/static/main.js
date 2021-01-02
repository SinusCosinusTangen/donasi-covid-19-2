$(function() {
    var acr = $('.accordion');
    var i;
    for (i = 0; i < acr.length; i++) {
        $('.accordion').eq(i).click(function() {
            this.classList.toggle("active");
            var panel = this.nextElementSibling;
            if (panel.style.maxHeight) {
                panel.style.maxHeight = null;
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px";
            }
        });
    }

});