import requests, re, bs4

html = requests.get(f'https://c.xkcd.com/random/comic/').text
soup = bs4.BeautifulSoup(html, 'html.parser')

transcript = soup.find('div', id='transcript')
comic_info = {
    'page_link': re.findall(r'Image URL \(for hotlinking\/embedding\)\: (.+)', transcript.previous_sibling)[0],
    'image_link': re.findall(r'Permanent link to this comic: (.+)', transcript.previous_sibling.previous_sibling.previous_sibling)[0],
}
print(comic_info)
