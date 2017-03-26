setInterval(function() {
    $.ajax({
        type: "GET",
        url: '/raw_position',  // URL to your view that serves new info
    })
    .done(function(response) {
        var positions = response.split('\n');
        for (var i=1; i<=5; i++) {
             var target = document.getElementById('pos' + i);
             target.innerHTML = positions[i];
             var slider = document.getElementById('pos' + i + '_slider');
             slider.value = positions[i];
             console.log(positions);
        }
    });
}, 1000);
