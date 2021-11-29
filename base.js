src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBwM32NKi7XSP0uVPI6pPp4YIEICkudsuE&callback=myMap">

function myMap() {
var mapProp= {
center:new google.maps.LatLng(51.508742,-0.120850),
zoom:5,
}
var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
}



