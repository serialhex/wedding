---
title: Home
---

<h2>Welcome</h2>

<script>

    CountDownTimer('09/27/2013 6:00 PM', 'countdown');

    function CountDownTimer(dt, id)
    {
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
                document.getElementById(id).innerHTML = 'EXPIRED!';

                return;
            }
            var days = Math.floor(distance / _day);
            var hours = Math.floor((distance % _day) / _hour);
            var minutes = Math.floor((distance % _hour) / _minute);
            var seconds = Math.floor((distance % _minute) / _second);

            document.getElementById(id).innerHTML = days + 'days ';
            document.getElementById(id).innerHTML += hours + 'hours ';
            document.getElementById(id).innerHTML += minutes + 'minutes ';
            document.getElementById(id).innerHTML += seconds + 'seconds';
        }

        timer = setInterval(showRemaining, 1000);
    }

</script>
<div id="countdown"></div>

Lorem Ipsum D0llar menu penuckle kangafoo-fu purple orange sasquach pickle salmon apricot in shoe llama zen monkey fork
