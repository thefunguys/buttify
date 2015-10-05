import subprocess
import os
from time import time
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    songs = [song for song in os.listdir('static') if '.wav' in song]
    return ' '.join(songs)
    

@app.route('/song/<song>')
def get_song():
    return 'song'


@app.route('/<album>')
def album_song(album):
    subprocess.call('./song.sh ' + album, shell=True)
    ts = str(int(time()))
    subprocess.call('cp static/song.wav static/' + ts + '.wav', shell=True)
    resp = make_response("<audio controls><source src=\"static/" + ts + ".wav\" type=\"audio/wav\"></audio>")
    resp.cache_control.no_cache = True
    return resp

if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
