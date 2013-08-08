---
title: Directions
image: directions.png
---

<!-- loads the maps api script -->
<script type="text/javascript"
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDiRQvTgbqeyWfx0LKgcVTibwvUnrt77rQ&sensor=false">
</script>

<!-- actual javascript... -->
<script type="text/javascript">
  var geocoder;
  var map;
  var directionsService = new google.maps.DirectionsService();
  var plaza = geocode('The Plaza, 884 17th St  Vero Beach, FL 32960');
  var ccvb = geocode('Cavalry Chapel, 941 18th St, Vero Beach, FL 32960');
  var directionsDisplay;

  function initialize() {
    var loc;
    directionsDisplay = new google.maps.DirectionsRenderer();
    geocode();
    var mapOptions = {
      center: ccvb,
      zoom: 18,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);
    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(document.getElementById("directionsPanel"));
  }

  function geocode(loc) {
    geocoder = new google.maps.Geocoder();
    // var latlng = new google.maps.LatLng(27.633866, -80.393003);
    geocoder.geocode( { 'address': loc}, function(results, status) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
      loc = results[0].geometry.location;
      // latlng = new google.maps.LatLng(loc.lat(), loc.lng());
    });
  }

  function calcRoute() {
    var start = document.getElementById("start").value;
    var request = {
      origin: start,
      destination: ccvb,
      travelMode: google.maps.TravelMode.DRIVING
    };
    directionsService.route(request, function(result, status) {
      if (status == google.maps.DirectionsStatus.OK) {
        directionsDisplay.setDirections(result);
      }
    });
  }

  google.maps.event.addDomListener(window, 'load', initialize);
</script>


<!-- the good stuff... -->

<!-- directions -->
<!-- http://www.sitepoint.com/find-a-route-using-the-geolocation-and-the-google-maps-api/ -->

# AHHHHHHHHHHHHH!!!!!!!!
UR GOIN THE RONG WAY!!!!!

<div id="directionsPanel"/>
<div id="map-canvas" class="map"/>
