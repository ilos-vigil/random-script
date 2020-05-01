import bs4, json, itertools, requests
from multiprocessing.dummy import Pool

output_file = open('acronym_abbreviation_id.json', 'w+')
base_link, total_page = 'http://kateglo.com/?&mod=abbr&phrase=&op=1&p=', 69
pool = Pool(8)

def grab(page_number):
    l = []
    html = requests.get(f'{base_link}{page_number}').text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for tr in soup.find('table').find_all('tr', {'valign': 'top'}):
        l.append(tr.find_all('td')[1].string)
    print(f'Done scrapping from page {page_number}')
    return l

list_all = pool.map(grab, [i for i in range(1, total_page + 1)])
list_all = list(itertools.chain.from_iterable(list_all))
pool.close()
pool.join()
json.dump(list_all, output_file)
