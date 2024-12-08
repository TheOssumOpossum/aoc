import sys
import re
sys.path.append('../..')
from lib.everybody_codes_read import read
lines, groups = read(__file__)

# p1
words = groups[0].split(':')[1].split(',')
# print(words)
sentence = groups[1]
s = 0
for w in words:
    s += len(re.findall(w, sentence))
print('p1', s)

#p2
sentences = groups[1].splitlines()
ss = set()
for w in words:
    for si, s in enumerate(sentences):
        for i in range(len(s)):
            s_short = s[i:]
            if s_short[:len(w)] == w:
                for j in range(len(w)):
                    ss.add((si, i+j))
    for si, s in enumerate(sentences):
        s = s[::-1]
        for i in range(len(s)):
            s_rev = s[i:]
            if s_rev[:len(w)] == w:
                for j in range(len(w)):
                    ss.add((si, len(s)-1-i-j))
print('p2', len(ss))
    
#p3
m = {}
for i in range(len(sentences)):
    for j in range(len(sentences[i])):
        m[(i,j)] = sentences[i][j]
directions = [(0,1),(1,0),(-1,0),(0,-1)]
symbols = set()
words2 = []
for w in words:
    words2.append(w[::-1])
words.extend(words2)
for w in words:
    for i in range(len(sentences)):
        for j in range(len(sentences[0])):
            for d in directions:
                tmp = set()
                for k in range(len(w)):
                    i_index = i + d[0]*k
                    j_index = j + d[1]*k
                    j_index %= len(sentences[0])
                    if (i_index, j_index) not in m:
                        break
                    if m[(i_index, j_index)] != w[k]:
                        break
                    else:
                        tmp.add((i_index, j_index))
                else:
                    symbols = symbols.union(tmp)
print('p3', len(symbols))
                
