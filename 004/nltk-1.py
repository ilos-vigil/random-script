from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet

text = '''Potato is a root vegetable native to the Americas, a starchy tuber of the plant Solanum tuberosum, and the plant itself, a perennial in the family Solanaceae.
Wild potato species can be found throughout the Americas, from the United States to southern Chile. The potato was originally believed to have been domesticated by indigenous peoples of the Americas independently in multiple locations, but later genetic testing of the wide variety of cultivars and wild species traced a single origin for potatoes. In the area of present-day southern Peru and extreme northwestern Bolivia, from a species in the Solanum brevicaule complex, potatoes were domesticated approximately 7,000–10,000 years ago. In the Andes region of South America, where the species is indigenous, some close relatives of the potato are cultivated. '''
sentences = sent_tokenize(text)
print(f'Kalimat : {sentences}')

first_word = word_tokenize(sentences[0])[0]
syn=wordnet.synsets(first_word)
print(f'Definisi {first_word} : {syn[0].definition()}')
