#!/usr/bin/env python

import json
import time
import ssl
from argparse import ArgumentParser
from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):

    def parse_json(self, string=None):
        try:
            decoded_string = string.decode("utf-8")
            parsed_json = json.loads(decoded_string)
        except:
            print("There was a problem parsing JSON.")
        else:
            if self.server.callback:
                self.server.callback(parsed_json)
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


class WebhookServer(HTTPServer):

    def __init__(self, callback=None, port=80, address="0.0.0.0", certfile=None, keyfile=None):
        server_address = (address, port)

        super(WebhookServer, self).__init__(server_address, RequestHandler)

        self.callback = callback

        if certfile:
            self.socket = ssl.wrap_socket(self.socket, certfile=certfile, keyfile=keyfile, server_side=True)

    def start(self):
        print(time.asctime(), "Server started @ %s:%s"
              % self.server_address)

        try:
            self.serve_forever()
        except KeyboardInterrupt:
            self.server_close()

        print(time.asctime(), "Server stopped @ %s:%s"
              % self.server_address)


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-a", "--address", action="store", dest="address",
                        help="specify address")
    
    parser.add_argument("-p", "--port", action="store", dest="port", type=int,
                        help="specify which port to listen")

    parser.add_argument("-c", "--certfile", action="store", dest="certfile",
                        help="certfile path")

    parser.add_argument("-k", "--keyfile", action="store", dest="keyfile",
                        help="keyfile path")

    args = parser.parse_args()

    print(args)

    if args.address and args.port:
        server = WebhookServer(address=args.address, port=args.port, certfile=args.certfile, keyfile=args.keyfile)
    elif args.address:
        server = WebhookServer(address=args.address, certfile=args.certfile, keyfile=args.keyfile)
    elif args.port:
        server = WebhookServer(port=args.port, certfile=args.certfile, keyfile=args.keyfile)
    else:
        server = WebhookServer(certfile=args.certfile, keyfile=args.keyfile)

    server.start()
