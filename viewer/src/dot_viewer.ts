// SPDX-FileCopyrightText: See AUTHORS file
//
// SPDX-License-Identifier: GPL-2.0-or-later

import * as d3 from "d3-graphviz";

export function init(injected_dot_graph: string | null) {
  let dot_str = null;
  if (injected_dot_graph) {
    dot_str = injected_dot_graph;
  } else if (location.hash.length > 1) {
    dot_str = decodeURIComponent(location.hash.substring(1));
  }

  const svg_div = document.getElementById("svg-div");
  const info_div = document.getElementById("info");

  window.addEventListener("unhandledrejection", () => {
    info_div.innerText = "Error generating graph, maybe it's too large.";
  });

  if (dot_str) {
    const graphviz = d3.graphviz(svg_div, {
      useWorker: false,
      zoomScaleExtent: [0.001, 100],
    });
    graphviz.renderDot(dot_str, () => {
      info_div.style.display = "none";
    });
  } else {
    info_div.innerHTML =
      "No dot graph provided. It can be provided by injecting it into the HTML file or by passing it as part of the url.";
  }
}
