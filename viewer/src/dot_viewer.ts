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

  const svg_container = document.getElementById("svg-div");

  if (dot_str) {
    d3.graphviz(svg_container, {
      useWorker: false,
      zoomScaleExtent: [0.001, 100],
    }).renderDot(dot_str);
  } else {
    svg_container.innerText =
      "No dot graph provided. It can be provided by injecting it into the HTML file or by passing it as part of the url.";
  }
}

export function show_dot_str(dot_str: string) {}