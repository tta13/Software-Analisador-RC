import glob, os
from posixpath import curdir
from flask import Flask, request, redirect, json

script_directory = os.getcwd()
data_dir = os.path.join(script_directory, 'data')

app = Flask(__name__)
app.config["UPLOADS"] = data_dir

@app.route('/matches', methods = ['GET'])
def get_matches():
    result = []
    if(os.getcwd() != data_dir):
        os.chdir(data_dir)
    for file in glob.glob("*.json"):
        result.append(file.split('.')[0])
    response = json.jsonify({ 'matches': result })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/matches/<match_id>/', methods = ['GET'])
def get_matches_analysis(match_id: str):    
    with open(os.path.join(data_dir, match_id + '.log.json')) as file:
        content = file.read()
        return content

def compare_extension(filename: str, expected_extension: str) -> bool:
    if not "." in filename or filename == '':
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() == expected_extension.upper():
        return True
    
    return False


@app.route('/upload', methods=['POST'])
def receive_upload():

    print('Request received')

    response = json.jsonify({'success': True, 'msg': ''})
    response.headers.add('Access-Control-Allow-Origin', '*')

    if request.method == 'POST':
        if request.files:

            rcg = request.files['rcg']
            rcl = request.files['rcl']
            if compare_extension(rcg.filename, 'RCG') and compare_extension(rcl.filename, 'RCL'):
                rcg.save(os.path.join(app.config['UPLOADS'], rcg.filename))
                
                rcl.save(os.path.join(app.config['UPLOADS'], rcl.filename))
        
            else:
                error = rcg.filename + ', ' + rcl.filename + ': file extension or name not allowed'
                print(error)
                response = json.jsonify({'success': False, 'msg': error})
                response.headers.add('Access-Control-Allow-Origin', '*')
                return  response

            print('Files saved')

            return response

    return response

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)