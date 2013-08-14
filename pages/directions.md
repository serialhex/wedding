---
title: Directions
image: map.png
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
  var plaza;
  var ccvb;
  var directionsDisplay;

  function initialize() {
    // var loc;
    plaza = geocode('The Plaza, 884 17th St  Vero Beach, FL 32960');
    ccvb = geocode('Cavalry Chapel, 941 18th St, Vero Beach, FL 32960');

    directionsDisplay = new google.maps.DirectionsRenderer();
    // geocode();
    var mapOptions = {
      center: ccvb,
      zoom: 18,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);
    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(document.getElementById("directionsPanel"));

    console.log(ccvb);
    map.setCenter(ccvb.location);
  }

  function geocode(loc) {
    geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': loc}, function(results, status) {
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
      return results[0];
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

Ceremony:  
Calvary Chapel, 941 18th St, Vero Beach  

Reception:  
The Plaza, 884 17th St  Vero Beach  

Ceremony is at 6pm on Friday September 27th at Calvary Chapel, Vero Beach.  The reception will be at The Plaza, right around the corner from the chapel at 6:30pm or so.  

*Remember to drop off you dish at the Plaza before joining us for the ceremony at 6*


<div id="directionsPanel"/>
<div id="map-canvas" class="map"/>
