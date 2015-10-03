import subprocess
from flask import Flask

app = Flask(__name__)
app.config.SERVER_NAME = 'localhost:8080'

@app.route('/')
def get_song():
    subprocess.call('./song.sh am', shell=True)
    return """<audio controls><source src="static/song.wav" type="audio/wav"></audio>"""   

if __name__=='__main__':
    app.run()
