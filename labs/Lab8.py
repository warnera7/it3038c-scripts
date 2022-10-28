#using the same venv as the webscraping.py
#using this link? - https://www.westbrockfuneralhome.com/store/flowers


from bs4 import BeautifulSoup
import requests

urlData = requests.get("https://www.westbrockfuneralhome.com/store/flowers").content
soup = BeautifulSoup(urlData, 'html.parser')

#name of item
a = soup.find("a", {"class":"product-title"})

itemName = a.text
#print(itemName)

#price of item
div = soup.find('div', {'class':'prices'})

itemPrice = div.text
#print(itemPrice)

#2 gets rid of he capital F, allowing me to format it better, 6 gets rid of from and the space
print('\n'"The flower arrangement %s can be purchased starting at %s." % (itemName,itemPrice[6:12]))