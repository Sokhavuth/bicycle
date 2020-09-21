#\app.py
import os
from bottle import route, run
   
@route('/')
def main():
    return "Hello World!"
   
if 'DYNO' in os.environ:
  run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
else: 
  run(host='localhost', port=5000, debug=True, reloader=True)