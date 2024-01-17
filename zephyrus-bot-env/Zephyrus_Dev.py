from flask import Flask, request, jsonify
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("TestEnv.env")
app = Flask(__name__)

currentTime = datetime.now()
def send_whapi_request(endpoint, params=None, method='POST'):
    headers = {
        'Authorization': f"Bearer {os.getenv('TOKEN')}"
    }
    url = f"{os.getenv('API_URL')}/{endpoint}"
    if params:
        if 'media' in params:
            details = params.pop('media').split(';')
            with open(details[0], 'rb') as file:
                m = MultipartEncoder(fields={**params, 'media': (details[0], file, details[1])})
                headers['Content-Type'] = m.content_type
                response = requests.request(method, url, data=m, headers=headers)
        elif method == 'GET':
            response = requests.get(url, params=params, headers=headers)
        else:
            headers['Content-Type'] = 'application/json'
            response = requests.request(method, url, json=params, headers=headers)
    else:
        response = requests.request(method, url, headers=headers)
    print('Whapi response:', response.json())
    return response.json()

def webhook_handler():
    # Data Code Here
    height = data['value']
    if height > threshold:
        # Trigger WhatsApp Bot
        send_whatsapp_message(height)

def send_whatsapp_message(value):
    url = "https://gate.whapi.cloud/messages/text?token=hLnmqrmxoMJxxa6krm8kHnfxjpNmEeg3"

    payload = {
        "typing_time": 0,
        "to": "120363219627523029@g.us",
        "body": f"""
🚨 *PERINGATAN DINI BANJIR* 🚨

Kepada Seluruh Warga Majalaya,

Status sungai Ci.. saat ini berada di level SIAGA IV.
Waspada terhadap datangnya banjir dan segeralah bersiap untuk melakukan evakuasi.
Detail Informasi:
    Tinggi Muka Air   : xx cm
    Kenaikan TMA     : xx cm
    Intensitas Hujan  : xx mm/jam
    Waktu Peringatan : {currentTime.strftime("%Y-%m-%d %H:%M:%S")}

Segera ambil tindakan pencegahan berikut ini:
    1. Tetap tenang dan jangan panik.
    2. Pindahkan barang berharga ke tempat yang lebih aman.
    3. Amankan dokumen penting.
    4. Ikuti petunjuk evakuasi dari pihak berwenang.

Jika Anda membutuhkan bantuan, hubungi nomor darurat berikut ini:
022-1110007

Terima Kasih atas perhatiannya, dan tetap waspada!

Salam,
Zephyrus
"""
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)

if __name__ == '__main__':
    port = os.getenv('PORT') or (443 if os.getenv('BOT_URL', '').startswith('https:') else 80)
    app.run(port=port, debug=True)