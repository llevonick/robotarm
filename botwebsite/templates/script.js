<script>
    var append_increment = 0;
    setInterval(function() {
        $.ajax({
            type: "GET",
            url: {% url 'display_updated_position' %},  // URL to your view that serves new info
            data: {'append_increment': append_increment}
        })
        .done(function(response) {
            $('#_appendHere').append(response);
            append_increment += 10;
        });
    }, 10000)
</script>
