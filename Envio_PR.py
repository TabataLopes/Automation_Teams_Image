import requests

def enviar_imagem_para_teams(imagem_path, grupo_id, token):
    url = f"https://graph.microsoft.com/v1.0/teams/{grupo_id}/channels/{canal_id}/messages"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    with open(imagem_path, 'rb') as imagem_arquivo:
        imagem_bytes = imagem_arquivo.read()

    payload = {
        "body": {
            "contentType": "html",
            "content": "<img src='data:image/jpeg;base64," + imagem_bytes.decode('utf-8') + "'/>"
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print("Imagem enviada com sucesso para o grupo Teams.")
    else:
        print("Falha ao enviar a imagem para o grupo Teams. Status code:", response.status_code)

# Exemplo de utilização
imagem_path = "Caminho_para_sua_imagem_local/imagem.jpg"
grupo_id = "/_#/conversations/48:notes?ctx=chat"
token = "SEU_TOKEN_DE_AUTORIZACAO"

enviar_imagem_para_teams(imagem_path, grupo_id, token)
