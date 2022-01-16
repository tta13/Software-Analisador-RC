import glob, os
from flask import Flask

script_directory = os.path.dirname(__file__)


app = Flask(__name__)

@app.route('/matches', methods = ['GET'])
def get_matches():
    result = []
    os.chdir(script_directory + '/data/')
    for file in glob.glob("*.json"):
        result.append(file.split('.')[0])
    return { 'matches': result }

@app.route('/matches/<match_id>/', methods = ['GET'])
def get_matches_analysis(match_id: str):    
    with open(script_directory + '/data/' + match_id + '.log.json') as file:
        content = file.read()
        return content
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)