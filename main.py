#from bs4 import BeautifulSoup

#with open("https://vk.com/friends?act=find") as fp:
#    soup = BeautifulSoup(fp)

#def not_lacie(href):
#    return href and not re.compile("lacie").search(href)
#soup.find_all (href=not_lacie)

import time
import ssl



try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass

else:
    ssl._create_default_https_context = _create_unverified_https_context

#import vk_api
from bs4 import BeautifulSoup
import urllib.request
import requests

#серверная авторизация
#def server_auth(self):
#    values = {
#        'client_id': self.app_id,
#        'client_secret': self.client_secret,
#        'v': self.api_version,
#        'grant_type': 'client_credentials'
#    }
#
#    response = self.http.post(
#        'https://oauth.vk.com/access_token', values
#    ).json()
#
#    if 'error' in response:
#        raise AuthError(response['error_description'])
#    else:
#        self.token = response
#-----------------------------------------------------------
#авторизация 2
#vk_session = vk_api.VkApi("login", "password")
#vk_session.auth()

#vk = vk_session.get_api()
#-----------------------------------------------------------
file = open("html.txt", "w+")
html_page = ('https://www.kmklegal.ru/')
soup = BeautifulSoup(html_page, 'html.parser')

for link in soup.findAll('a', class_=('div')):
    time.sleep(5)
    print(link.get('href'))
response = requests.post(html_page, files={"form_field_name": file})
if response.ok:
    file = open("html.txt", "w+")
    file.write(response.text)
    file.close()
    print("Загрузка прошла успешно")
    #print(response.text)
else:
    print("Ёпта, не работает")





