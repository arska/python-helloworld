import textwrap,os

from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world from {0}</h1>
                <p>{1}</p>
            </body>
            </html>
        '''.format(os.environ.get('HOSTNAME', 'here'), os.environ.get('MESSAGE', 'Hello, world!')))
        self.wfile.write(response_text.encode('utf-8'))

server_address = ('', 3000)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
