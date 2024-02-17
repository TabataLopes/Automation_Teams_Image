import requests
import base64
from dotenv import load_dotenv
import os

load_dotenv()

# Path da imagem no SharePoint
image_url = os.getenv('IMG_PATH') 

# Lendo imagem transformando em bytes
with open(image_url, "rb") as img_file:
    img_bytes = img_file.read()

# Codifica os bytes da imagem em base64
img_base64 = base64.b64encode(img_bytes).decode('utf-8')

# URL do seu webhook do Microsoft Teams
webhook_url = os.getenv('WEBHOOK_URL')

# Monta o Adaptive Card com a imagem
adaptive_card_json = {
    "type": "message",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "body": [
                    {
                        "type": "Image",
                        "url": f"data:image/png;base64,{img_base64}",
                        "altText": "Descrição da Imagem"
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.4"
            }
        }
    ]
}

# Configura os cabeçalhos da solicitação para o Microsoft Teams
headers = {"Content-Type": "application/json"}

# Envia o Adaptive Card com a imagem para o webhook do Microsoft Teams
response_teams = requests.post(webhook_url, json=adaptive_card_json, headers=headers, stream=True)

# Verifica se a solicitação para o Microsoft Teams foi bem-sucedida
if response_teams.status_code == 200:
    print("Adaptive Card com imagem do SharePoint enviado com sucesso para o webhook do Microsoft Teams.")
else:
    print("Falha ao enviar o Adaptive Card com imagem do SharePoint para o webhook do Microsoft Teams. Status code:", response_teams.status_code)
