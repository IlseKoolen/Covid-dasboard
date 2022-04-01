from requests import get

import logging

def download_summary():
  '''''
  Send HTTP request to API /summary and return the response in JSON format.

  API details: https://documenter.getpostman.com/view/10808728/SzS8rjbc#00030720-fae3-4c72-8aea-ad01ba17adf8
  '''''

  #Send the HTTP request
  response=get(f'https://api.covid19api.com/summary')
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