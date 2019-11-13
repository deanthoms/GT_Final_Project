// from data.js
var tableData = data;

var filter = d3.select("#filter-btn");

filter.on("click", function() {
    var alien_input = d3.select("#datetime");
    
    var alien_date = alien_input.property("value");

    var specific_alien_sitings = tableData.filter(siting => siting.datetime === alien_date);

    var dates = specific_alien_sitings.map(siting => siting.datetime);
    var cities = specific_alien_sitings.map(siting => siting.city);
    var states = specific_alien_sitings.map(siting => siting.state);
    var countries = specific_alien_sitings.map(siting => siting.country);
    var shapes = specific_alien_sitings.map(siting => siting.shape);
    var durations = specific_alien_sitings.map(siting => siting.durationMinutes);
    var comments = specific_alien_sitings.map(siting => siting.comments);

    var tbody = d3.select("tbody");
    var row = tbody.append("tr");

    tbody.html("");

    for (var i = 0; i < dates.length; i++) {
        row.append("td").text(dates[i]);
        row.append("td").text(cities[i]);
        row.append("td").text(states[i]);
        row.append("td").text(countries[i]);
        row.append("td").text(shapes[i]);
        row.append("td").text(durations[i]);
        row.append("td").text(comments[i]);
        var row = tbody.append("tr");
    }
});