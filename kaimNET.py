#Veri Kazıma
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://deprem.afad.gov.tr/'

#url'i açıp, sayfayı alma
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html pars etme
page_soup = soup(page_html, "html.parser")


son_depremler_div = page_soup.findAll("div",{"class":"sag"})

depremler = son_depremler_div[0].ul

#son deprem olan şehiri getir
#sehir = depremler.li.div.text


# ['İL','TARİH|SAAT','DEPREM BÜYÜKLÜĞÜ','Detay']
son_5_deprem = []
for city in  depremler.find_all('li'):
    #cities = city.li.div.text
    #print(city)
    son_5_deprem.append(list(city.stripped_strings))



#print(son_5_deprem)
# SON 5 DEPREM BÖLGESİ ve BÜYÜKLÜKLERİ
"""for i in range(5):
son_5_deprem[i][2] = int(son_5_deprem[i][2])
    print(son_5_deprem[i][0], son_5_deprem[i][2])

    if((son_5_deprem[i][2])>1):
        print("Büyük deprem")"""


# Büyüklük {4.5} ve üstü olduğu zaman tetikle
i = 1
while True:
    son_5_deprem[i][2] = float(son_5_deprem[i][2])
    if((son_5_deprem[i][2])>4.5):
        print(son_5_deprem[i][0], son_5_deprem[i][2])
        print("Büyük deprem oldu. Sistem Tetiklendi!")
    i = i + 1
    if(i ==5 ):
        break

