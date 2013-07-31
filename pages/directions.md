---
title: Directions
image: directions.png
---

<!-- move this somewhere nice later -->
<style type="text/css">
  /*#map-canvas { height: 480px; width: 640px; }*/
</style>

<!-- loads the maps api script -->
<script type="text/javascript"
  src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDiRQvTgbqeyWfx0LKgcVTibwvUnrt77rQ&sensor=false">
</script>

<!-- actual javascript... -->
<script type="text/javascript">
  var geocoder;
  var map;
  var directionsService = new google.maps.DirectionsService();
  var latlng;
  var directionsDisplay;

  function initialize() {
    var loc;
    directionsDisplay = new google.maps.DirectionsRenderer();
    geocode();
    var mapOptions = {
      center: latlng,
      zoom: 17,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);
    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(document.getElementById("directionsPanel"));
  }

  function geocode() {
    geocoder = new google.maps.Geocoder();
    // var latlng = new google.maps.LatLng(27.633866, -80.393003);
    geocoder.geocode( { 'address': 'Cavalry Chapel, 941 18th St, Vero Beach, FL'}, function(results, status) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
      loc = results[0].geometry.location;
      latlng = new google.maps.LatLng(loc.lat(), loc.lng());
    });
  }

  function calcRoute() {
    var start = document.getElementById("start").value;
    var request = {
      origin: start,
      destination: latlng,
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

# AHHHHHHHHHHHHH!!!!!!!!
UR GOIN THE RONG WAY!!!!!

<div id="map-canvas" style="float:left;width:70%; height:480px"/>
<div id="directionsPanel" style="float:right;width:30%;height: 480px"/>
