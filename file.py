import http.server
import socketserver

PORT= 8000

reqHandler= http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT),reqHandler) as directory:
	print("Server started at localhost: " + str(PORT))
	directory.serve_forever()
