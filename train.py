from keras.preprocessing.text import text_to_word_sequence

with open('data/obama.txt', 'r') as f:
    obama_raw = f.read()
with open('data/trump.txt', 'r') as f:
    trump_raw = f.read()


