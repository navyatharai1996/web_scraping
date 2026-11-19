
import csv
from pathlib import Path
from urllib.request import urlopen
from bs4 import BeautifulSoup   

url = "https://realpython.github.io/fake-jobs/"

with urlopen(url, timeout=30) as response:
    html = response.read().decode("utf-8")

#print("Page downloaded successfully")
#print("Characters downloaded:", len(html))

soup = BeautifulSoup(html, "html.parser")

##job_titles = soup.find_all("h2", class_="title")

##for title in job_titles:
   ## print(title.get_text(strip=True))

job_cards = soup.find_all("div", class_="card-content")

keywords = ["python", "software", "data"]
results = []
for job in job_cards:
    title = job.find("h2", class_="title").get_text(strip=True)
    company = job.find("h3", class_="company").get_text(strip=True)
    location = job.find("p", class_="location").get_text(strip=True)

    for keyword in keywords:
        if keyword in title.lower():
            results.append({
                "title": title,
                "company": company,
                "location": location,
                "matched_keyword": keyword
         })
            print(title)
            print(company)
            print(location)
            print("Matched keyword:", keyword)
            print()
            break

print("Total matching jobs:", len(results))

