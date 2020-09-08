function disableScroll() {
    // Get the current page scroll position
    scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,

        // if any scroll is attempted, set this to the previous value
        window.onscroll = function() {
            window.scrollTo(scrollLeft, scrollTop);
        };
}

function getCookie(cname) {
     var name = cname + "=";
     var ca = document.cookie.split(';');
     for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if(c.indexOf(name) == 0)
           return c.substring(name.length,c.length);
     }
     return "";
}

$(document).ready(function(){
//    disableScroll();
    $('#raw_material_tab').click(function(){
//        alert("tab_clicked");
        console.log("Hiiiiiiiii");


    });

    function get_suppliers(po_no){
        var ajax_url='/api/get_suppliers';
        post_data = {"po_no":po_no}
        $.post(ajax_url,
            {'csrfmiddlewaretoken': getCookie('csrftoken'), "data": JSON.stringify(post_data)},
            function(data, status){
                if(data)
                {
                    $('#id_Supplier').val(data);
                    $('#id_inv_NO').val(Math.floor(Math.random() * 1111));
                }
                else
                {
                    alert("Please check for another Purchase Order Number");
                    $('#id_Supplier').val("");
                    $('#id_inv_NO').val("");
                    $('#final_amount').empty();
                    $('#purchase_orders_table').empty();
                    return false;

                }

            }
        );
        return true;
    }

    $(document).bind('keypress', function(e) {
        var po_no = $('#id_R1_PO_NO').val()
        if(e.keyCode==13){
        		get_suppliers(po_no)
         }
    });
});



