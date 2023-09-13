import os
import sys
from time import sleep
from random import choice

s = """( {C}{nuc}\033[0m(     ){Ccom}{com}\033[0m )
 `-.`. ,',-'
    _,-'"
 ,-',' `.`-.
"""

complements = {'A':'T','T':'A','C':'G','G':'C'}
colors = {'A':'\033[92m', 'C':'\033[94m', 'G':'\033[93m','T':'\033[91m'}
# A: green, C: blue, G: yellow, T:red
# ENDC = '\033[0m'
os.system('clear')

i = 0
while True:
    i += 1
    for line in s.splitlines():
        nuc = choice('ACGT')
        print('\t',line.format(nuc=nuc,com=complements[nuc],C=colors[nuc],Ccom=colors[complements[nuc]]))
        sys.stdout.flush()
        sleep(0.2)
 
