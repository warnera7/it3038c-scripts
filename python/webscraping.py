#call from the venv and specify the path location, use python <path>
from bs4 import BeautifulSoup
import requests, re

# STUFF BEFORE THE SECOND TO LAST EXAMPLE
r = requests.get('http://webscraper.io/test-sites/e-commerce/allinone/phones').content
soup = BeautifulSoup(r, 'html.parser')
print(type(soup))
print(soup.prettify()[:100])

for link in soup.find_all('a'): print(link.get('href'))
#for link in soup.find_all('a', attrs={'href':re.compile("^https://github.com")}):
 #   print(link)

# tags = soup.findAll("a", {"href":re.compile('[<>#%|\{\}!\\^~\[\]`/]')})
# for a in tags:
#         print(a.get('href'))

# # SECOND EXAMPLE TRYING TO FIND THE DIV TAGS
# r = requests.get('http://webscraper.io/test-sites/e-commerce/allinone/phones').content
# soup = BeautifulSoup(r, 'html.parser')

# tags = soup.findAll("div", {"class":re.compile('(ratings)')})
# for p in tags:
#     a = p("p", {"class":"pull-right"})
#     print(a[0].string)


# # THIRD EXAMPLE OF WEBSCRAPING, THIS TIME USING REEBOK.COM
# data = requests.get("https://www.reebok.com/us/flexagon-energy-shoes---preschool/DV8354.html").content
# soup = BeautifulSoup(data, 'html.parser')

# span = soup.find("h1", {"class":"name___120FN"})
# title = span.text

# span = soup.find("div", {"class":"gl-price-item notranslate"})
# price = span.text
# print("Item %s has price %s" % (title,price))