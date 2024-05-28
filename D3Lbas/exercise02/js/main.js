/*
*    main.js
*/

var svg = d3.select("#chart-area").append("svg")
	.attr("width", 400)
	.attr("height", 400);

var data = [25, 20, 15, 10, 5];

var dataShow = d3.select("#dataShow").append("svg")
	.attr("width", 400)
	.attr("height", 400);

var bars = dataShow.selectAll("rect").data(data);


var barHeight = 200;
var marginBottom = 20;
bars.enter().append("rect")
            .attr("x", (d, i) => {
                console.log("Item: " + d + " index: "+ i);
                console.log((i * 60) + 50); 
                return ((i * 60) + 50);
            })
            .attr("y", (d) => {
                return barHeight - d - marginBottom + 200;
            })
            .attr("height", (d) => { return d; })
            .attr("width", 50)
            .attr("fill", "green");

dataShow.append("rect")
    .attr("x", 0) 
    .attr("y", 0) 
    .attr("width", 400) 
    .attr("height", 400) 
    .attr("fill", "none") 
    .attr("stroke", "black") 
    .attr("stroke-width", 2); 