$(function(){
    $(".search-box").keyup(function(){
        var element = $(".search-box").val()
        
        $.ajax({
            url: '/question/all?q=' + element,
            success : function(e) {
                $(".content").empty();

                if(e.length != 0) {
                    for (i=0; i <e.length; i++) {
                        $(".content").append(`
                        <div class="row align-items-center">
                            <a href="/question/` + e[i].id + `" style="">` + e[i].question + `</a>
                            
                        </div>
                        <hr style="margin-left: 5%; margin-right: 5%; margin-top: 0;">
                        `)
                    }
                } else {
                    $(".content").append(`
                    <div class="row align-items-center justify-content-center" style="margin: 5%;">
                        <h1>There are no question</h1>
                    </div>
                    `)
                }
            }
        })
    })
})