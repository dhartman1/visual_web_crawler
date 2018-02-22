var svg = d3.select("svg"),
    margin = 20,
    width = svg.node().getBoundingClientRect().width,
    diameter = +svg.attr("height"),
    g = svg.append("g").attr("transform", "translate(" + width / 2 + "," + diameter / 2 + ")");

// Center graph on window resize
$( window ).resize(function() {
  width = svg.node().getBoundingClientRect().width,
  diameter = +svg.attr("height"),
  g.attr("transform", "translate(" + width / 2 + "," + diameter / 2 + ")");
});

var color = d3.scaleLinear()
    .domain([-1, 5])
    .range(["hsl(152,80%,80%)", "hsl(228,30%,40%)"])
    .interpolate(d3.interpolateHcl);

var pack = d3.pack()
    .size([diameter - margin, diameter - margin])
    .padding(2);

root = JSON.parse(d3.select("#search_json").text());

root = d3.hierarchy(root)
    .sum(function(d) {
      if (!('children' in d)) {
        return 1;
      }
    })
    .sort(function(a, b) { return b.value - a.value; });

var focus = root,
    nodes = pack(root).descendants(),
    view;

var circle = g.selectAll("circle")
  .data(nodes)
  .enter().append("circle")
    .attr("class", function(d) { return d.parent ? d.children ? "node" : "node node--leaf" : "node node--root"; })
    .style("fill", function(d) { return d.children ? color(d.depth) : null; })
    .on("mouseover", function(d) { d3.select("#child_url").text(d["data"]["url"]); })
    .on("mouseout", function(d) { d3.select("#child_url").text(""); })
    .on("click", function(d) { if (focus !== d) zoom(d), d3.event.stopPropagation(); });

var text = g.selectAll("text")
  .data(nodes)
  .enter().append("text")
    .attr("class", "label")
    .attr("alignment-baseline", "middle")
    .style("fill-opacity", 0)
    .style("display", "inline")
    .style("font-size", 11)
    .text(function(d) { return d.data.domain; });

var node = g.selectAll("circle,text");

svg.on("click", function() { zoom(root); });

zoomTo([root.x, root.y, root.r * 2 + margin]);
$("#parent_url").attr("href", root['data']['url']).text(root['data']['url']);
scaleAllText(root);

// Enable pointer events for leaf nodes whose parent is the root node
d3.selectAll("circle")
  .filter(function(d) { return d.parent === root && this.classList.contains("node--leaf") })
  .style("pointer-events", "auto");

function zoom(d) {
  $("#parent_url").attr("href", d['data']['url']).text(d['data']['url']);
  var focus0 = focus; focus = d;

  var transition = d3.transition()
      .duration(d3.event.altKey ? 7500 : 750)
      .tween("zoom", function(d) {
        var i = d3.interpolateZoom(view, [focus.x, focus.y, focus.r * 2 + margin]);
        return function(t) { zoomTo(i(t)); };
      });

  transition.selectAll("text")
    .filter(function(d) { return d.parent === focus || this.style.display === "inline"; })
    .style("fill-opacity", 0)

  transition.selectAll("circle")
    .filter(function(d) { return (d.parent === focus || this.style.pointerEvents === "auto" ) && this.classList.contains("node--leaf"); })
    .style("pointer-events", function(d) { return d.parent === focus ? "auto" : "none"; });

  transition.on("end", function() { scaleAllText(focus); });
}

function zoomTo(v) {
  var k = diameter / v[2]; view = v;
  node.attr("transform", function(d) { return "translate(" + (d.x - v[0]) * k + "," + (d.y - v[1]) * k + ")"; });
  circle.attr("r", function(d) { return d.r * k; });
  circle.each(function(d) { d.circleWidth = this.getBBox().width; });
}

// Scale all text elements
function scaleAllText(parent) {
  d3.selectAll("text")
    .filter(function(d) { return d.parent && (d.parent === parent); })
    .each(function(d) { scaleText(this, d); } )
    .transition()
    .duration(500)
    .style("fill-opacity", 1);
}

// Scale a single text element
function scaleText(element, data) {
  var circleWidth = data.circleWidth;
  var textWidth = element.getBBox().width;
  var prevFontSize = parseFloat(element.style.fontSize);
  var newFontSize = prevFontSize * (circleWidth / textWidth);
  element.style.fontSize = newFontSize;
}

// Scroll on page load
window.onload = function() {
  $('html, body').animate({scrollTop: $('#scroll_here').offset().top}, 800);
};
