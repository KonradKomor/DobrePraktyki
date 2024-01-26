import socketserver
import random
from http.server import BaseHTTPRequestHandler
import requests

class LoadBalancerHandler(BaseHTTPRequestHandler):
    BACKEND_SERVERS = [
        ('localhost', 5001),
        ('localhost', 5002),
        ('localhost', 5003),
        ('localhost', 5004),
        ('localhost', 5005)
    ]

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        backend_server = self.select_backend_server()
        self.proxy_to(backend_server)

    def select_backend_server(self):
        return random.choice(self.BACKEND_SERVERS)

    def proxy_to(self, backend_server):
        target_url = f'http://{backend_server[0]}:{backend_server[1]}/'
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len)

        # Przekierowanie żądania POST do wybranego backendu
        response = requests.post(target_url, data=post_body, headers=self.headers)

        # Przekazanie odpowiedzi z backendu do klienta
        self.send_response(response.status_code)
        for key, value in response.headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(response.content)

def run_load_balancer(port=8080):
    with socketserver.TCPServer(("", port), LoadBalancerHandler) as http:
        print(f"Load balancer działa na {port}")
        http.serve_forever()

if __name__ == '__main__':
    run_load_balancer()