// SPDX-FileCopyrightText: See AUTHORS file
//
// SPDX-License-Identifier: GPL-2.0-or-later

import * as d3 from "d3-graphviz";

const dot_str = decodeURIComponent(location.hash.substring(1));
d3.graphviz("#svg-div", { useWorker: false }).renderDot(dot_str);
