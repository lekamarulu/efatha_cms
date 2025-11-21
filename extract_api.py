import requests, json

url = "https://yourdomain.com/swagger.json"
data = requests.get(url).json()

for path, methods in data.get("paths", {}).items():
    for method in methods.keys():
        print(f"{method.upper()} {path}")
