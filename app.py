#!/usr/bin/python3
import logging
from routers.api_v1 import HTTPServer, HTTPReqHandler

def app():
    server = HTTPServer(('0.0.0.0', 8080), HTTPReqHandler)
    logging.info('Starting httpd...\n')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
    logging.info('Stopping httpd...\n')
    
if __name__ == '__main__':
    app()
