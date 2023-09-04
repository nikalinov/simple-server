from http.server import HTTPServer, BaseHTTPRequestHandler


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes('<html><body><h1>You are now connected to the server!</h1></body></html>', 'utf-8'))
