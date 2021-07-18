$(function () {
    $("#kmeans").click(function () {
	$.getJSON('/kmeans/',
                function(data) {
              $("#me").css("visibility", "visible");
        	$("#me").html(data);
        });
        
    })
    $("#iso").click(function () {
	$.getJSON('/isolation/',
                function(data) {
              $("#me").css("visibility", "visible");
        	$("#me").html(data);
        });
        
    })
    $("#hbos").click(function () {
	$.getJSON('/hbos/',
                function(data) {
              $("#me").css("visibility", "visible");
        	$("#me").html(data);
        });
        
    })
})
