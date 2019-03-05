import requests
from bs4 import BeautifulSoup

r = requests.get("http://pythonhow.com/example.html")
conntent = r.content
soup = BeautifulSoup(conntent, "html.parser")
city_divs = soup.find_all("div", {"class":"cities"})
for city in city_divs:
    a = city.find("h2").text
    b = city.find("p").text
    print(a,"\n",b)
