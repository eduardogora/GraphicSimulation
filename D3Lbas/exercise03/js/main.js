/*
*    main.js
*/
var info = [];

var svg = d3.select("#chart-area").append("svg")
	.attr("width", 800)
	.attr("height", 400);

svg.append("rect")
    .attr("x", 0) 
    .attr("y", 0) 
    .attr("width", 800) 
    .attr("height", 400) 
    .attr("fill", "none") 
    .attr("stroke", "black") 
    .attr("stroke-width", 2); 

d3.csv("../../resources/data/ages.csv").then((data)=> {
    //console.log("CSV");
    //console.log(data);
});

d3.tsv("../../resources/data/ages.tsv").then((data)=> {
    //console.log("TSV");
    //console.log(data);
});


d3.json("../../resources/data/ages.json").then((data)=> {
    console.log("JSON");
    console.log(data);
    data.forEach((d)=>{
		d.age = +d.age;
	});
    info = data;

    
    var circles = svg.selectAll("circle").data(info);

    circles.enter().append("circle")
            .attr("cx", (d, i) => {
                console.log("Item: " + d + " index: "+ i);
                return ((i+1) * 125);
            })
            .attr("cy", (d) => {
                return 100;
            })
            .attr("r", (d) => { return d.age * 5; })
            .attr("fill", (d) => {return d.age < 11 ?  "green" : "red"});

}).catch((error) => {
    console.error("El archivo no existe");
});



