---
title: Home
image: mainpage.png
---

<script>

    CountDownTimer('09/27/2013 6:00 PM', 'countdown');

    function CountDownTimer(dt, id) {
        var end = new Date(dt);

        var _second = 1000;
        var _minute = _second * 60;
        var _hour = _minute * 60;
        var _day = _hour * 24;
        var timer;

        function showRemaining() {
            var now = new Date();
            var distance = end - now;
            if (distance < 0) {
                clearInterval(timer);
                document.getElementById(id).innerHTML = 'WED WE SHALL BE!';
                return;
            }
            var days = Math.floor(distance / _day);
            var hours = Math.floor((distance % _day) / _hour);
            var minutes = Math.floor((distance % _hour) / _minute);
            var seconds = Math.floor((distance % _minute) / _second);

            // document.getElementById(id).innerHTML = 'Countdown to the wedding:<br>'
            document.getElementById(id).innerHTML = days     + ' days ';
            document.getElementById(id).innerHTML += hours   + ' hours ';
            document.getElementById(id).innerHTML += minutes + ' minutes ';
            document.getElementById(id).innerHTML += seconds + ' seconds</div>';
        }

        timer = setInterval(showRemaining, 1000);
    }

</script>
<div id="countdown-txt" class="strokeme count">Countdown to the wedding:<br></div>
<div id="countdown" class="strokeme count">loading...</div>

Welcome to Justin and Megan's Wedding Website. Feel free to browse the site whenever you need a refresher on time or place or to get an idea of what to give us for a gift. If you have any questions either ask us in person or click on either email at the bottom of the pages to send us a note. We hope to see you at the Party!
