import requests, re, bs4, pprint

html = requests.get('https://www.cnnindonesia.com/').text
soup = bs4.BeautifulSoup(html, 'html.parser')

daftar_berita = []
for article in soup.find_all('div', class_='list media_rows')[2].find_all('article'):
    link = article.a.attrs['href']
    judul = article.find('span', class_='box_text').h2.string
    kategori = article.find('span', class_='box_text').find('span', class_='kanal').string
    daftar_berita.append({'link': link,'judul': judul,'kategori': kategori})
pprint.pprint(daftar_berita)
