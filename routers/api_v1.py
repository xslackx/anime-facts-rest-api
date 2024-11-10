import json
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
import urllib.parse
from controllers.api_v1 import (
    v1_get_facts, 
    v1_get_facts_by_id, 
    v1_get_animes
    )

class HTTPReqHandler(BaseHTTPRequestHandler):

    def HTTP_OK(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
    def do_GET(self):
  
        self.query_dict = urllib.parse.parse_qs(self.path)
        base = self.path.split('/')
        limit_query = 25
        
        if base == ['', 'api'] or base == ['', 'api', '']:
            self.HTTP_OK()
            self.wfile.write(json.dumps({"message": "consult /api/v1 to see all animes supported"}).encode())
            self.log_request(200, 'OK')
            self.close_connection
            
        # get '/api/:anime_name' v1_get_facts(req, res)
        elif len(self.query_dict) == 1  and len(self.query_dict['/api/v1/?q']) == 1:
             query = self.query_dict['/api/v1/?q'][0].split(",")
             if len(query) <= limit_query:
                 if len(query) == 1:
                     self.HTTP_OK()
                     if v1_get_facts(query[0], self.wfile):
                         self.log_request(200, 'OK')
                         self.close_connection
                 else:
                     pass
                     # bulk query
                     
        # get_facts_by_id
        elif len(self.query_dict) == 2 and len(self.query_dict.get("i")) > 0:
            fact_id = int(self.query_dict.get('i')[0])
            anime_name = self.query_dict.get('/api/v1/?q')[0]
            self.HTTP_OK()
            if v1_get_facts_by_id((anime_name, fact_id), self.wfile):
                self.log_request(200, 'OK')
                self.close_connection
             
        # get '/api/v1' all animes  
        elif base == ['', 'api', 'v1'] or base == ['', 'api', 'v1', '']:
            self.HTTP_OK()
            if v1_get_animes('all', self.wfile):
                self.log_request(200, 'OK')
                self.close_connection
                             
        # get '/' home     
        elif len(self.path.split('/')) == 2 and self.path.split('/')[0] == '':
            self.HTTP_OK()
            data = json.dumps({"message": "Anime Facts Rest Python API"})
            self.wfile.write(data.encode('utf-8'))
            self.close_connection
        else:
            self.send_response(404, "Not found")
            self.close_connection
        
        self.end_headers()