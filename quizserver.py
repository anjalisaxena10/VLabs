import BaseHTTPServer
import SocketServer
import re
import json
from Models.repository import Repository

httpd = None
keep_running = True

class QuizServer(BaseHTTPServer.BaseHTTPRequestHandler):
    TCP_PORT = 54321

    def do_GET(self):
        print "path: ", self.path
        self.serveRequest()

    def getIdentifier(resource):
        return int(resource.split('/')[-1])

    def serveRequest(self):
        resource = self.path.lower()
        response = 200
        content_type = "text/json"
        repo = Repository()

        # get all labs (http://localhost:54321/Labs)
        if resource == "/labs" or resource == "/labs/":
            body = repo.getAllLabs()

        # get a specific lab (http://localhost:54321/Labs/1)
        elif None != re.search('/labs/*', resource):
            identifier = self.getIdentifier(resource)
            body = repo.getLab(identifier)

        # get all Experiment, questions for a lab (http://localhost:54321/ExperimentQuizzes/1)
        elif None != re.search('/experimentquizzes/*', resource):
            identifier = self.getIdentifier(resource)
            body = repo.getExperimentQuizes(identifier)

        # didn't match any return invalid response
        else:
            body = "unknown request"
            content_type = "text/html"
            response = 400

        self.send_response(response)
        self.send_header("Content-type", content_type)
        self.send_header("Content-Length", len(body))

        self.end_headers()
        self.wfile.write(body)

SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("127.0.0.1", QuizServer.TCP_PORT), QuizServer)
keep_running = True
print " print 'HTTP Server Running....serving at port", QuizServer.TCP_PORT
while keep_running:
    httpd.handle_request()
exit(0)









