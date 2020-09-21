#\app.py
from bottle import route, run
   
@route('/')
def main():
    return "Hello World!"
   
run(host='localhost', port=9000, debug=True, reloader=True)