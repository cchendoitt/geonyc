from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
app = Flask(__name__)

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/parse', methods=['POST'])
def geocoding():
   location = request.form.get('name')

   if len(location.strip()) == 0:
       return render_template('index.html', location = 'No location entered!')

   from bigapple.parser import BigAppleParser
   p = BigAppleParser()
   #parsed = p.parse(location.upper())
   parsed = p.parse(location)
   standardized_address = parsed['components']['output_address']
   
   json_object = json.dumps(parsed) 
   #return render_template('index.html', location = location, name = json_object)
   response = app.response_class(
        response=json_object,
        mimetype='application/json'
    )
   return response
if __name__ == '__main__':
   app.run(debug=True)
   #app.run(host= '0.0.0.0')