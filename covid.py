from requests import get
import logging

#create a constant 'URL_API' with the URL of the API
URL_API='https://api.covid19api.com'

def download_summary():
  '''''
  Send HTTP request to API /summary and return the response in JSON format.

  API details: https://documenter.getpostman.com/view/10808728/SzS8rjbc#00030720-fae3-4c72-8aea-ad01ba17adf8
  '''''

  #Send the HTTP request
  response=get(f'{URL_API}/summary')
  #Check for the HTTP response status 200 (OK)
  if response.status_code==200:
    #return the response as JSON
    return response.json()
  #Otherwise, something went wrong  
  else:
    #Show the error message
    logging.error(f'An error has occured:HTTP status {response.status_code}')
    #Return an empty result
    return{}

def download_conformed_per_country(country):
  '''''
  Send HTTP request to API /country/<country>/status/confirmed to receive the daily number of confirmed cases for the requested country. Return the response in JSON format.

  API details: https://documenter.getpostman.com/view/10808728/SzS8rjbc#b07f97ba-24f4-4ebe-ad71-97fa35f3b683

  country -- the name of the requested
  '''''
  #send HTTP request
  response=get(f'{URL_API}/country/{country}/status/confirmed')
  #check for the HTTP response status 200 (OK)
  if response.status_code==200:
    #  Return the response as JSON
    logging.info('Successfully received Dutch data from COVID19 API')
    return {'data':response.json()}
  #Otherwise, something went wrong
  else:
    #show the error message
    logging.error(f'An error has occured: HTTP status {response.status_code}')
    #return an empty result
    return{}