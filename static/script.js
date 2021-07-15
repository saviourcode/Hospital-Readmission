$(function () {
    $("#test").click(function () {
	$.getJSON('/kmeans/',
                function(data) {
              $("#me").css("visibility", "visible");
        	$("#me").html(data);
        });
        
    })
})
