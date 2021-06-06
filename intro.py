import http.server
import socketserver

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path== '/':
			self.path= 'intro.html'
		return http.server.SimpleHTTPRequestHandler.do_GET(self)

reqHandler= HttpRequestHandler

port= 8000
server= socketserver.TCPServer(("", port), reqHandler)
print("Server started at "+ str(port))
print("\nUse <Ctrl-C> to close the server connection")

server.serve_forever()
