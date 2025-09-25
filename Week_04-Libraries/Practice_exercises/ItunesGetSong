import json
import requests
band = str(input("Type a singer/band name: "))
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + band)

o = response.json()
for result in o["results"]:
    print(result["trackName"])