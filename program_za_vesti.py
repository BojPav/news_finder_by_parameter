from BeautifulSoup import BeautifulSoup

import requests

page = requests.get('http://www.24ur.com/novice/svet/')

soup = BeautifulSoup(page.content)

for link in soup.findAll("a"):
    if "ZDA" in link:
        print link

#print soup.html


#if "srbija" in soup:
    #print soup

'''for link in soup.find("table", attrs={"class": "wikitable"}).findAll("a"):
    if link.string == "season":

        season_5 = requests.get("https://en.wikipedia.org/wiki/Game_of_Thrones_(season_5)" + link["href"])

        osebna_stran_soup = BeautifulSoup(season_5.content)

        tabela = osebna_stran_soup.find("table", attrs={"class": "wikitable plainrowheaders wikiepisodetable"})

        stevilo_gledalcev = BeautifulSoup(tabela)





        for row in tabela.findAll("td"):

            stevilo_gledalcev = tabela.findAll("td")

            print row.text'''