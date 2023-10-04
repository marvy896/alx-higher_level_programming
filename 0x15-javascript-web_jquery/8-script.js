$.getJSON('https://swapi.co/api/films/?format=json',
  function (data) {
    $.each(data.movies, function (index, movie) {
