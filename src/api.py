import requests

def get_gpt_response(message):
    url = "https://api.zpi.my.id/v1/ai/gpt-4-turbo"
    headers = {"Accept": "application/json"}
    payload = {
        "messages": [
            {"role": "system", "content": "Nama Anda adalah Zaileys AI"},
            {"role": "user", "content": message}
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    try:
        response_json = response.json()
        return response_json
    except ValueError:
        print("Error: Unable to parse JSON response")
        print(response.text)
        return None