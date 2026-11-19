from urllib.request import urlopen

url = "https://realpython.github.io/fake-jobs/"

with urlopen(url, timeout=30) as response:
    html = response.read().decode("utf-8")

print("Page downloaded successfully")
print("Characters downloaded:", len(html))