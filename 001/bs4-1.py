import requests, re, bs4, pprint

daftar_berita = []
html = requests.get(f'https://news.ycombinator.com/').text
soup = bs4.BeautifulSoup(html, 'html.parser')

for p in soup.find_all("tr", class_="athing"):
    title = p.find_all('td', class_='title')[1].a.string
    source = p.find_all('td', class_='title')[1].a.attrs['href']
    points = None if p.next_sibling.td.next_sibling.find('span', class_='score') is None else p.next_sibling.td.next_sibling.find('span', class_='score').string
    points = 0 if type(points) is not bs4.element.NavigableString else int(re.search(r'[\d]+', points)[0])
    age = 0 if p.next_sibling.td.next_sibling.find('span', class_='age').a is None else p.next_sibling.td.next_sibling.find('span', class_='age').a.string
    comment_count = None if len(p.next_sibling.td.next_sibling.find_all('a')) < 3 else p.next_sibling.td.next_sibling.find_all('a')[3].string
    comment_count = 0 if type(comment_count) is not bs4.element.NavigableString or comment_count == 'discuss' else int(re.search(r'[\d]+', comment_count)[0])
    daftar_berita.append({'title': title, 'source': source, 'points': points, 'age': age, 'comment_count': comment_count})
pprint.pprint(daftar_berita)
