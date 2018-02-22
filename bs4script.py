import requests
page = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html5lib')
f = open("fpl.json", "w+")
f.write(str(soup.body.contents[0]))
f.close()