import requests

link = "https://news.google.com/?tab=wn&hl=en-US&gl=US&ceid=US:en"
f = requests.get(link)
print(f.text)