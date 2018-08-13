import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
    
def create_session():
  req_session = requests.Session()
  retries = Retry(total=5,
                  backoff_factor=0.1,
                  status_forcelist=[400, 500, 502, 503, 504])
  req_session.mount('http://', HTTPAdapter(max_retries=retries))
  return req_session

def do_get(self, url, headers):
  result = None
  req_session = self.create_session()
  response = req_session.get(url, headers=headers)
  if response.status_code == 200:
      result = response.json()
  return result
