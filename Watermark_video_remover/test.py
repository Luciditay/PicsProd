import requests

URL_to_download: str = ""
file_destination: str = ""

res = requests.get(URL)
res.raise_for_status()

with open(file_destination, "+bw", encoding= "utf-8") as file