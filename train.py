from keras.preprocessing.text import text_to_word_sequence
from keras.preprocessing.text import hashing_trick

SAMPLE_WORDS = 6000

with open('data/obama.txt', 'r') as f:
    obama_raw = f.read()
with open('data/trump.txt', 'r') as f:
    trump_raw = f.read()

obama_seq = text_to_word_sequence(obama_raw)[:SAMPLE_WORDS]
trump_seq = text_to_word_sequence(trump_raw)[:SAMPLE_WORDS]

obama_words = set(obama_seq)
obama_vocab = len(obama_words)
trump_words = set(trump_seq)
trump_vocab = len(trump_words)

# Integer encoding
obama_encoding = hashing_trick(obama_raw, round(obama_vocab*1.3), hash_function='md5')
trump_encoding = hashing_trick(obama_raw, round(obama_vocab*1.3), hash_function='md5')

print(obama_encoding)
