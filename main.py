from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Lab2 : Google App Engine. Deployed succesfully'
