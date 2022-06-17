# import libraries
from bs4 import BeautifulSoup
import requests

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


# data = {}
# for table, heading in zip(gdp_table_data[1].find_all("table"), headings):
#     t_headers = []
#     for th in table.find_all("th"):
#         t_headers.append(th.text.replace('\n', ' ').strip())
    
#     table_data = []
#     for tr in table.tbody.find_all("tr"):
#         t_row = {}
#         for td, th in zip(tr.find_all("td"), t_headers):
#             t_row[th] = td.text.replace('\n', '').strip()
#         table_data.append(t_row)
    
#     data[heading] = table_data

# print(data)