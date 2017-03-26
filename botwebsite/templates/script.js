<script>
    setInterval(function() {
        $.ajax({
            type: "GET",
            url: '/position_raw.html',  // URL to your view that serves new info
        })
        .done(function(response) {
            var positions = response.split('\n');
            for (var i=1; i<=5; i++) {
              var target = document.getElementById('pos' + i);
              target.innerHTML = positions[i-1];
            }
        });
    }, 1000)
</script>
