from requests import Session
from .captcha_resolver import resolve_captcha
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

bac_link = "https://bac.onec.dz/"

def make_request(matricule,code,brute_force=None) : 
    sess = Session()
    sess.verify= False
    response = sess.get(bac_link)
    data = {
    'token': "",
    'matricule': matricule,
    'pwd': code,
    'cap': str(resolve_captcha(response.text)),
    'result': '',
        }
    return sess.post(bac_link,
                    data=data).text
