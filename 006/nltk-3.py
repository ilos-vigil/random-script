from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from pprint import pprint

text = 'Arch Linux adheres to five principles: simplicity, modernity, pragmatism, user centrality and versatility. In general, the principles maintain minimal distribution-specific changes, minimal breakage with updates, pragmatic over ideological design choices, user-friendliness, and minimal bloat.'
sentences = sent_tokenize(text)

for sentence in sentences:
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    print(f'Sentence : {sentence}')
    print('Part of Speech tagging :')
    pprint(tagged_words)
