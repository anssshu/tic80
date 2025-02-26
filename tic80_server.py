import http.server
import socketserver
import webbrowser
import threading
import msvcrt
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# Define the handler to serve the HTML file
class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Serve files from the current directory
        return os.path.join(current_dir, path.lstrip('/'))

# Define the server
PORT = 8000
httpd = socketserver.TCPServer(('', PORT), CustomHTTPRequestHandler)

# Function to start the server
def start_server():
    print(f'Serving at port {PORT}')
    webbrowser.open(f'http://localhost:{PORT}/index.html')
    httpd.serve_forever()

# Start the server in a separate thread
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Wait for the ESC key to stop the server
print('Press ESC to stop the server')
while True:
    if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':  # ESC key
        print('Stopping the server...')
        httpd.shutdown()
        server_thread.join()
        break
print('Server stopped')