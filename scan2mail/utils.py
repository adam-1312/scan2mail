from urllib.parse import urlencode, quote
import qrcode
import requests
import base64
import io

from random import randint as rr

API_TOKEN = ''

def generate_qr(to, subject, body):
    url = f'mailto:?{urlencode({"to":to,"subject":subject,"body":body},quote_via=quote)}'

    # Shorten mailto link using tinyurl api
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    params = {
        'api_token': API_TOKEN,
    }

    json_data = {
        'url': url,
        'domain': 'tinyurl.com',
        'alias': f'adamstest{rr(0,100000)}',
        'description': 'string',
    }

    response = requests.post('https://api.tinyurl.com/create', params=params, headers=headers, json=json_data)
    tiny_url = response.json()['data']['tiny_url']
    print(response.json()) # For logging

    # Generate qr code in base64
    qr = qrcode.make(tiny_url)
    in_mem_file = io.BytesIO()
    qr.save(in_mem_file, format="PNG")
    in_mem_file.seek(0)
    img_bytes = in_mem_file.read()
    b64 = base64.b64encode(img_bytes).decode("utf-8")
    
    return tiny_url, b64
