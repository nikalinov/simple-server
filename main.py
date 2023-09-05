from http.server import HTTPServer, BaseHTTPRequestHandler
import time


HOST = '10.183.72.107'
PORT = 8000


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes('<html><body><h1>You are now connected to the server!</h1></body></html>', 'utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.wfile.write(bytes(f'{{"time": "{date}"}}', 'utf-8'))


server = HTTPServer((HOST, PORT), Server)
print('Server is running...')
server.serve_forever()
server.server_close()
print('Server stopped.')
