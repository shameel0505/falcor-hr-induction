# -*- coding: utf-8 -*-
"""
Falcor HR Induction - Local Dev Server & Interactive Console Launcher
Starts an HTTP server and opens your default browser automatically.
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

def get_free_port(start_port):
    import socket
    port = start_port
    while port < start_port + 50:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('localhost', port)) != 0:
                return port
            port += 1
    return start_port

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)

    port = get_free_port(PORT)
    url = f"http://localhost:{port}/"

    handler = http.server.SimpleHTTPRequestHandler
    
    print("=" * 65)
    print("  Falcor HR Induction - Interactive Presenter Console")
    print("=" * 65)
    print(f" Serving directory : {base_dir}")
    print(f" Local URL          : {url}")
    print(" Shortcuts          : Space (Play/Pause), Left/Right (Slides), M (Mute)")
    print(" Press Ctrl+C in this terminal to stop the server.")
    print("=" * 65)

    webbrowser.open(url)

    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped gracefully.")

if __name__ == '__main__':
    main()

