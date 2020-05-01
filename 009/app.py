import bs4
import nltk
import json
import re
import requests

with open('./acronym_abbreviation_id.json', 'r') as f:
    data = f.read()
    list_acronym_abbreviation = json.loads(data)

from_wikipedia = False
if from_wikipedia:
    # Take text with Indonesian language from Wikipedia randomly
    html = requests.get('https://id.wikipedia.org/wiki/Istimewa:Halaman_sembarang').text
    soup = bs4.BeautifulSoup(html, 'html.parser')

    for p in soup.find('div', class_='mw-parser-output').find_all('p'):
        text = f'{text}{p.get_text()}'
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\[\d*\]', '', text)
else:
    text = '''
Linux (atau GNU/Linux, lihat kontroversi penamaannya) adalah nama yang diberikan kepada kumpulan sistem operasi Mirip Unix yang menggunakan Kernel Linux sebagai kernelnya. Linux merupakan proyek perangkat lunak bebas dan sumber terbuka terbesar di dunia. Seperti perangkat lunak bebas dan sumber terbuka lainnya pada umumnya, kode sumber Linux dapat dimodifikasi, digunakan dan didistribusikan kembali secara bebas oleh siapa saja
'''
    text = re.sub(r'\n', '', text)
print(f'Input : {text}')

# pisah berdasarkan kalimat
# step 1
boundary = '•'
rule = {
    r'\.': f'.•',
    r'\?': f'?•',
    '!': f'!•',
    ';': f';•',
    ':': f':•'
}
for old, new in rule.items():
    text = re.sub(old, new, text)

# step 2
for word in re.finditer(r'"(.+)"', text):
    start_position, end_position = word.regs[0][0], word.regs[0][1]
    quoted_sentence = text[start_position:end_position]
    quoted_sentence = re.sub('•', '', quoted_sentence) # remove boundary
    if text[end_position] == '.': # move boundary if character after " is . 
        text = text[:start_position] + quoted_sentence + text[end_position:]
    else:
        text = text[:start_position] + quoted_sentence + '•' + text[end_position:]

# step 3
for word in re.finditer(r'([\w]*)(\.|\?|!|;|:)•', text): # [word][sign]•
    # [0] -> position start, [1] -> position for [word], [2] -> position for [sign]
    # position value is adalah (start, end + 1)

    word_start_position, word_end_position, boundary_position = word.regs[1][0], word.regs[2][1], word.regs[0][1]

    if text[word_start_position:word_end_position] in list_acronym_abbreviation:
        text = text[:word_end_position] + text[boundary_position:] # remove boundary

# step 4
for word in re.finditer(r'([\w]+) ?(!|\?)(•) ?[a-z]', text): #[word](optional space)[sign][•](optional space)[lowercase char]
    boundary_position = word.regs[2][1]
    text = text[:boundary_position] + text[boundary_position:]

# step 5
sentences = text.split('•')
print('Output:')
[print(s.lstrip(' ').rstrip(' ')) for s in sentences]
