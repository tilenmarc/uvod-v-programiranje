from http.server import HTTPServer, BaseHTTPRequestHandler


webpage = b"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>My page</title>
</head>
<body>
    <h1>Hello from Python</h1>
    <p>This page at UVP lectures.</p>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(webpage)


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), Handler)
    print("Serving on http://localhost:8000")
    server.serve_forever()
