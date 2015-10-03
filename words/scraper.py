from bs4 import BeautifulSoup
from nltk.corpus import wordnet
import requests
import re

band = 'arctic-monkeys'
album = 'am'

songs = BeautifulSoup(requests.get('http://www.songlyrics.com/' + band + '/' + album + '/').text, "lxml")

for l in songs.find_all(href=re.compile(band)):
    soup = BeautifulSoup(requests.get(l['href']).text, "lxml")

    lyrics = soup.find('p', id='songLyricsDiv')
    if not lyrics:
        continue
    for word in lyrics.get_text().split():
        new = wordnet.morphy(word)
        if new:
            print word, 

    print ' '
