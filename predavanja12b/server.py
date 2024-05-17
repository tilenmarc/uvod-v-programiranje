import http.server
import socketserver

moj_port = 8888
moj_html = "preprost.html"


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

    def vrni_vsebino(self, po_do_vsebine):
        with open(po_do_vsebine, mode="r", encoding="utf-8") as f:
            vsebina = f.read()
        return bytes(vsebina, "utf-8")

    def do_GET(self):
        print(self.path)
        self._set_headers()
        vsebina = self.vrni_vsebino(moj_html)
        self.wfile.write(vsebina)


with socketserver.TCPServer(("", moj_port), MyHttpRequestHandler) as httpd:
    print("http server deluje na portu", moj_port)
    httpd.serve_forever()
