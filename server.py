import http.server
import socketserver

PORT = 5000

handler_object = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler_object) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
