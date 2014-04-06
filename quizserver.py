import BaseHTTPServer
import SocketServer

httpd = None
keep_running = True

class QuizServer(BaseHTTPServer.BaseHTTPRequestHandler):
    TCP_PORT = 54321

    def do_GET(self):
        print "path: ", self.path

        self.serveRequest()

    def readQuizzes(self):
        return "{'result': true, 'count': 1, 'quizzes': [{'quiz': [10, 20, 30, 40], 'ans': 50}]}"

    def readRequestedResource(self, path):
        try:
            resource = open(path)
            content = resource.read()
            resource.close()
            return (True, content)
        except:
            return (False, "")

    def serveRequest(self):
    	resource = self.path.lower()
        response = 200
        content_type = "text/html"

        if resource == "/main.html" or resource == "/main.html/":
            res, body = self.readRequestedResource("html/main.html")
            content_type = "text/html"
        elif resource == "/scripts/xhr.js" or resource == "/scripts/view.js" or resource == "/styles/style.css":
            res, body = self.readRequestedResource(resource[1:])
            assert(res)
            if resource[-3:] == ".js":
                content_type = "text/javascript"
            elif resource[-4:] == ".css":
                content_type = "text/css"
        elif resource == "/quizzes" or resource ==  "/quizzes/":
            body = self.readQuizzes()
            content_type = "text/json"
        elif resource == "/stop" or resource ==  "/stop/":
            print "will stop next!!"
            global keep_running
            keep_running = False

            body="{'result': true}"
        else:
            body = "unknown request"
            response = 400

        self.send_response(response)
        self.send_header("Content-type", content_type)
        self.send_header("Content-Length", len(body))

        self.end_headers()
        self.wfile.write(body)


SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("127.0.0.1", QuizServer.TCP_PORT), QuizServer)
keep_running = True

print "serving at port", QuizServer.TCP_PORT
while keep_running:
    httpd.handle_request()

exit(0)








