from flask import Flask, request
import logging
from datetime import datetime
import json

app = Flask(__name__)

logging.basicConfig(filename='./logs/webhook.log', level=logging.INFO)

@app.route('/', defaults={'path': ''}, methods=['POST', 'GET'])
@app.route('/<path:path>', methods=['POST', 'GET'])
def webhook(path):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    method = request.method
    try:
        json_data = request.json if request.json else {}
    except Exception as e:
        json_data = {}
    form_data = request.form.to_dict()
    log_data = {
        'timestamp': timestamp,
        'method': method,
        'path': path,
        'json_data': json_data,
        'form_data': form_data
    }
    logging.info(json.dumps(log_data))
    return {"status": "success"}, 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
