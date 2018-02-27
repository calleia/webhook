#!/usr/bin/env python

import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 80


def parse_json(self):
    try:
        j = json.loads(self)
    except:
        print("ERRO")
    else:
        print(j)


class RequestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        response = self.path.encode("utf8")

        self.wfile.write(response)

    def do_POST(self):

        content_len = int(self.headers["content-length"])
        post_body = self.rfile.read(content_len)

        self.send_response(200)
        self.end_headers()

        parse_json(post_body)

        return


if __name__ == "__main__":

    server_address = (HOST, PORT)

    httpd = HTTPServer(server_address, RequestHandler)

    print(time.asctime(), "Server started @ %s:%s" % server_address)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()

    print(time.asctime(), "Server stopped @ %s:%s" % server_address)
