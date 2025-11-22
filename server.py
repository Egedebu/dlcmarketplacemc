import http.server
import socketserver
import webbrowser
import os

PORT = 8000  # İstersen burayı değiştirebilirsin
FOLDER = os.path.dirname(os.path.abspath(__file__))  # Bu dosyanın bulunduğu klasör

os.chdir(FOLDER)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"Eaglercraft live server başlatıldı: http://localhost:{PORT}")
print("Tarayıcı açılıyor...")

# Tarayıcıyı otomatik aç
webbrowser.open(f"http://localhost:{PORT}/index.html")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer kapatıldı.")
    httpd.server_close()
