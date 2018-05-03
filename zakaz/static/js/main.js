/**
 * Created by User5454 on 24.04.2018.
 */
url1 ="https://rosreestr.ru/wps/PA_RRORSrviceExtended/Servlet/ChildsRegionController?parentId=102000000000"
$(document).ready(function(){

$( "select" )
  .change(function() {
    var str = "";
    $( "select option:selected" ).each(function() {
      str += $( this ).attr('id');
     var a1= parseInt( str);
    if(a1 !== a1)
    {
        $("#num").text("0");
    }
    else {
        $("#num").attr("value").parseInt( str).val();//  выбранный id региона
         var nab = parseInt( str);
         console.log(nab);
        //window.location.href=nab
    }
    });
   })
  .trigger( "change" );


});

