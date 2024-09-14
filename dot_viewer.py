def show(dot_graph: str):
    import tempfile
    import webbrowser
    import urllib.parse
    from pathlib import Path
    import base64

    current_dir = Path(__file__).parent.absolute()
    viewer_path = current_dir / Path("viewer/dist/dot_viewer.html")
    js_path = current_dir / Path("viewer/dist/dot_viewer.js")

    with open(viewer_path) as f:
        html = f.read()

    str_encoded = base64.b64encode(dot_graph.encode("utf-8")).decode("utf-8")
    html = html.replace("dot_viewer.js", str(js_path))
    html = html.replace(
        "injected_dot_graph = null", f"injected_dot_graph = atob(`{str_encoded}`)"
    )

    with tempfile.NamedTemporaryFile(
        delete=False, suffix=".html", prefix="dot_viewer_"
    ) as tmp_html_file:
        tmp_html_file.write(html.encode("utf-8"))
        html_file_path = tmp_html_file.name

    url = f"file://{html_file_path}"
    webbrowser.open(url)
