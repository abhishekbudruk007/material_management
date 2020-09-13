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

$(document).ready(function() {
      var ajax_url='/api/get_stock_details';
     $.post(ajax_url,
            {'csrfmiddlewaretoken': getCookie('csrftoken')},
            function(data, status){
                if(data){
                    var data = JSON.parse(data) ;
                    console.log("data",data);
                    console.log("Type of ",typeof(data));
                    record = []

                    for(var i=0; i<data.length; i++)
                    {
                        data_to_push = {}
                        data_to_push["pk"] = data[i]["pk"]
                        data_to_push["R1_MaterilQty"] = data[i]["fields"]["R1_MaterilQty"]
                        data_to_push["R1_MaterilUnit"] = data[i]["fields"]["R1_MaterilUnit"]
                        data_to_push["R1_RowMatShape"] = data[i]["fields"]["R1_RowMatShape"]
                        data_to_push["R1_RowMatSize"] = data[i]["fields"]["R1_RowMatSize"]
                        data_to_push["R1_RowMatType"] = data[i]["fields"]["R1_RowMatType"]
                        record.push(data_to_push);
                    }
                    console.log("records",record)
                    bind_data_to_table(record)
                }
            });
});





function bind_data_to_table(data)
{

    var table = $('#stock_details_table').DataTable( {
            "pageLength": 5,
            "aaData": data,
            "lengthMenu": [ [5,10,25,50,100,-1], [5,10,25,50,100,"All"] ],
            "columns": [
//                { "data": '<a href="Cutting/?pk={{ n2.id }}">pk</a>', defaultContent: ''},
                { "data": "pk", "name": "pk",
                    fnCreatedCell: function (nTd, sData, oData, iRow, iCol) {
                        $(nTd).html("<a href='Cutting/?pk="+oData.pk+"'>"+oData.pk+"</a>");
                    }
                },
                { "data": 'R1_RowMatSize', defaultContent: '' },
                { "data": 'R1_RowMatShape', defaultContent: '' },
                { "data": 'R1_RowMatType', defaultContent: ''},
                { "data": 'R1_MaterilQty', defaultContent: ''},
                { "data": 'R1_MaterilUnit', defaultContent: '' },
             ]
        });

}

//var table = $('#stock_details_table').DataTable( {
//        "pageLength": 10,
////        lengthMenu: [ [5,10,25,50,100,-1], [5,10,25,50,100,"All"] ],
//		"bJQueryUI": true,
//		"paging": true,
//		"select": true,
//        "destroy": true,
//        "processing": true,
//        "serverSide": true,
//        "aaSorting": [],
//        "ajax": "{% url 'get_stock_details' %}",
//    });