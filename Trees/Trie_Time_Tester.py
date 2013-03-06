#Michael Robertson
#mirob2005@gmail.com
#Completed: 3/5/2013

import time
from Trie_Prefix_Count import Trie as Trie_space
from Trie_Prefix_Count_Speed import Trie as Trie_speed

t = Trie_space()

start = time.clock()
print('Start Trie Space: %s'%start)

fileIn = open('../Lorem_ipsum.txt','r').read()
words = fileIn.split(' ')

for word in words:
    t.add(word)
    
wordTime = time.clock()
print('Words added in: %f'%(wordTime-start))

wordFindTime = time.clock()
print('Found pellentesque value = %s in %f'%(t.getValue('pellentesque'),(wordFindTime - wordTime)))

t = Trie_speed()
start = time.clock()
print('Start Trie Speed: %f'%start)

fileIn = open('../Lorem_ipsum.txt','r').read()
words = fileIn.split(' ')

for word in words:
    t.add(word)
    
wordTime = time.clock()
print('Words added in: %f'%(wordTime-start))

wordFindTime = time.clock()
print('Found pellentesque value = %s in %f'%(t.getValue('pellentesque'),(wordFindTime - wordTime)))