
# Software-Analisador-RC

This app performs RoboCup 2D soccer log analysis! The application consists of a **frontend**, where you can upload Log files and gather analysis from matches and of a **backend** where the requests from the frontend and the extraction of statistics are made.

### System requirements
- [Node.js](https://nodejs.org/pt-br/)
- [Angular 13](https://angular.io/)
- [Python 3](https://www.python.org/)
- [Docker](https://www.docker.com/)

## Running the project (frontend and backend)
Run the backend application in a docker container:
```bash 
$ ./build-image.sh
$ docker-compose up
```
Or in the command line:
```bash 
$ cd backend
$ pip install -r requirements.txt
$ python3 ./flask_app.py
```
In a new command line, run the frontend application:
```bash
$ cd frontend
$ npm install
$ npm start
```
Wait for the compilation and, when it completes, go to [`http://localhost:4200/`](http://localhost:4200/) to see the aplication running.

## Running the analysis only
To perform the analysis of a match, in a command line, run:
```bash 
$ cd backend
$ python3 ./run.py --rcg path/to/file_name.rcg --rcl path/to/file_name.rcl --output path/to/output_file.json
```
Or simply:
```bash 
$ cd backend
$ python3 ./run.py --rcg path/to/file_.rcg --rcl path/to/file_name.rcl
```