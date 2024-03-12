from http.server import BaseHTTPRequestHandler
from urllib import parse
import json
from sinkaf import Sinkaf

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Assuming the POST request is a JSON with a 'phrases' key
        data = json.loads(post_data.decode('utf-8'))
        phrases = data.get('phrases')

        if phrases:
            snf = Sinkaf()
            prediction = snf.tahmin(phrases)
            likelihood = snf.tahminlik(phrases)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'prediction': prediction.tolist(),  # Convert numpy array to list
                'likelihood': likelihood.tolist()
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Please provide phrases'}).encode())

