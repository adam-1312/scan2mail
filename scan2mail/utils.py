from urllib.parse import urlencode, quote, quote_plus
import qrcode
import requests
import base64
import io

def generate_qr(to, subject, body, api_key, cc='', bcc='', alias=None):
    url = f'mailto:?{urlencode({"to":to,"cc":cc,"bcc":bcc,"subject":subject,"body":body},quote_via=quote)}'

    # Shorten mailto link using tinyurl api
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    params = {
        'api_token': api_key,
    }

    if alias is None:
        alias = quote_plus(subject).replace('+','-')
    json_data = {
        'url': url,
        'domain': 'tinyurl.com',
        'alias': alias,
        'description': 'string',
    }

    response = requests.post('https://api.tinyurl.com/create', params=params, headers=headers, json=json_data)
    
    print(params)
    print(json_data)
    print(response.json()) # For logging
    
    tiny_url = response.json()['data']['tiny_url']

    # Generate qr code in base64
    qr = qrcode.make(tiny_url)
    in_mem_file = io.BytesIO()
    qr.save(in_mem_file, format="PNG")
    in_mem_file.seek(0)
    img_bytes = in_mem_file.read()
    b64 = base64.b64encode(img_bytes).decode("utf-8")
    
    return tiny_url, b64
