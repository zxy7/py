
import requests
import bs4
response = requests.get('http://www.jlhzby.com/park/carrierInfo.aspx')

soup = bs4.BeautifulSoup(response.text, "html.parser")

soup.select('table.mbtable')
# for item in soup.select('table.mbtable'):
#   print(item.get_text())  
print(soup.get_text())  