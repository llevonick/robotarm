function postSlider(slider) {
  angle = document.getElementById('pos' + slider + '_slider').value
  servo = slider - 1 + '';
  endpoint = '/set_servo?servo=' + servo + '&angle=' + angle;
  $.ajax({
    type: 'GET',
    url: endpoint,
  }).done(function(response) {});
}
