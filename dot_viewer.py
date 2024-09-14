def show(dot_graph: str):
    import webbrowser
    import urllib.parse
    from pathlib import Path

    viewer_path = Path(__file__).parent / Path("viewer/dist/dot_viewer.html")

    str_encoded = urllib.parse.quote(dot_graph)
    url = f"file://{viewer_path}#{str_encoded}"
    webbrowser.open(url)
