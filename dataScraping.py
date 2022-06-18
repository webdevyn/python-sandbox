# import libraries
from bs4 import BeautifulSoup
import requests
import csv

url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# make a GET request to fetch raw HTML content
html_content = requests.get(url).text

# parse HTML content
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())   #print parsed html data

# print(soup.title)  # print title with html tags
# print(soup.title.text)   # print title with no tags

# for link in soup.find_all("a"):
#     print("Inner text: {}".format(link.text))
#     print("Title: {}".format(link.get("title")))
#     print("href: {}".format(link.get("href")))

gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.find_all("tr")

headings = []
for th in gdp_table_data[0].find_all("th"):
    headings.append(th)

print(headings)

