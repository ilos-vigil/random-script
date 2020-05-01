from nltk.corpus import wordnet

word_list = ['Computer', 'Like', 'Enjoy', 'NLP', 'Angry']

for word in word_list:
    synonyms, antonyms = [], []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas(): 
            synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    print(f'Synonym for {word} : {synonyms}')
    print(f'Antonym for {word} : {antonyms}')
