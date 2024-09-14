// SPDX-FileCopyrightText: See AUTHORS file
//
// SPDX-License-Identifier: GPL-2.0-or-later

const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { library } = require("webpack");

module.exports = {
  entry: "./src/dot_viewer.ts",
  plugins: [
    new HtmlWebpackPlugin({
      template: "./src/dot_viewer.html",
      filename: "dot_viewer.html",
      inject: "head",
      scriptLoading: "blocking",
    }),
  ],
  output: {
    filename: "dot_viewer.js",
    path: path.resolve(__dirname, "dist"),
    clean: true,
    library: "dot_viewer",
  },
  mode: "production",
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
    ],
  },
};
