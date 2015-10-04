from bs4 import BeautifulSoup
from nltk.corpus import wordnet
import requests
import re

band = 'fergie'
album = 'the-dutchess'

songs = BeautifulSoup(requests.get('http://www.songlyrics.com/' + band + '/' + album + '/').text, "lxml")

for l in songs.find_all(href=re.compile(band)):
    soup = BeautifulSoup(requests.get(l['href']).text, "lxml")

    lyrics = soup.find('p', id='songLyricsDiv')
    if not lyrics:
        continue
    text = lyrics.get_text().encode('ascii', 'ignore')
    text = re.sub('<.+?>', '', text);
    text = re.sub('\\[.+?\\]', '', text);
    text = re.sub('\\(.+?\\)', '', text);
    print text
