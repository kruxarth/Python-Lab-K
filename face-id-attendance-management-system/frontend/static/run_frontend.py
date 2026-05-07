import http.server
import socketserver
import webbrowser
import threading

PORT = 8080

def start_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 Serving at http://localhost:{PORT}")
        httpd.serve_forever()

# Open browser automatically
webbrowser.open(f"http://localhost:{PORT}")

# Start server
threading.Thread(target=start_server).start()
