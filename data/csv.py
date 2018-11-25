# Number of words included in each file/sample
LENGTH = 100

with open('obama.txt') as f:
    o_raw = f.read()
o_words = o_raw.split(' ')
with open('trump.txt') as f:
    t_raw = f.read()
t_words = t_raw.split(' ')

f_num = 0
while len(o_words) >= LENGTH and len(t_words) >= LENGTH:
    f_num += 1
    with open('obama/%d' % f_num, 'w') as f:
        for i in range(LENGTH):
            f.write(o_words.pop(0) + ' ')
    with open('trump/%d' % f_num, 'w') as f:
        for i in range(LENGTH):
            f.write(t_words.pop(0) + ' ')

