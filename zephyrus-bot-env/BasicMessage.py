import requests
from datetime import datetime

url = "https://gate.whapi.cloud/messages/text?token=hLnmqrmxoMJxxa6krm8kHnfxjpNmEeg3"

currentTime = datetime.now()

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
