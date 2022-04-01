# Import the object Flask from the flask module
from flask import Flask
from covid import download_summary, download_conformed_per_country

#import and setup logging
import logging
log_format = "[%(levelname)s] - %(asctime)s : %(message)s in %(module)s:%(lineno)d"
logging.basicConfig(filename='covid.log', format=log_format, level=logging.INFO)

import json

# Create a webserver object called 'COVID Dashboard' and keep track of it in the variable called server
server=Flask('COVID dashboard')

# Define an HTTP route / to serve the dashboard home web page
@server.route('/')
# Define the function 'index()' and connect it to the route /
def index():
# Return the static file 'index.html'
  return server.send_static_file('index.html')

# Define an HTTP route /summary to serve the summary chart
@server.route('/summary')
# Define the function 'serve_summary()' and connect it to the route /summary
def serve_summary():
  #load JSON template from sumary.json
  json_template=json.load(open('templates/summary.json'))
  #download summary from COVID API
  json_data=download_summary()
  #Add the data to the template
  json_template['data']['values']=json_data['Countries']
  #Send the chart description to the client
  return json_template


# Define an HTTP route /new to serve the new count worldwide chart
@server.route('/new')
# Define the function 'serve_summary_new()' and connect it to the route /new
def serve_summary_new():
# Return the string "A pie chart summary of new COVID cases globally."
  return 'A pie chart summary of new COVID cases globally.'

# Define an HTTP route /netherlands to serve the chart of the Netherlands
@server.route('/netherlands')
# Define the function 'serve_netherlands_history()' and connect it to the route /netherlands
def serve_netherlands_history():
# Return the string "An area chart of COVID cases over time in the Netherlands."
  return download_conformed_per_country('netherlands')

# Start the webserver
server.run('0.0.0.0')