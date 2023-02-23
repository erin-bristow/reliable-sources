import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Wikipedia:Reliable_sources/Perennial_sources"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find("table", class_ = "perennial-sources")

for row in table.tbody.find_all("tr"):
	columns = row.find_all("td")
	#print(columns)

	if(columns != []):
		try:
			print(columns[0].find('a')['title'])
		except (TypeError, KeyError):
			# Probably occuring because the source does not have a linked Wikipedia page.
			# Instead, just print text.
			print(columns[0].text)
