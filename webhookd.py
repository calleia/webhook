#!/usr/bin/env python

import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def parse_json(self, string=None):
        try:
            decoded_string = string.decode("utf-8")
            parsed_json = json.loads(decoded_string)
        except:
            print("There was a problem parsing JSON.")
        else:
            print(parsed_json)

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

        self.parse_json(post_body)

        return


class WebhookServer():

    def __init__(self, port=80, address="0.0.0.0"):

        server_address = (address, port)

        self.server = HTTPServer(server_address, RequestHandler)

    def start(self):
        print(time.asctime(), "Server started @ %s:%s"
              % self.server.server_address)

        try:
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.server.server_close()

        print(time.asctime(), "Server stopped @ %s:%s"
              % self.server.server_address)


if __name__ == "__main__":
    server = WebhookServer()
    server.start()
