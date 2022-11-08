import ssl



try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass

else:
    ssl._create_default_https_context = _create_unverified_https_context

from bs4 import BeautifulSoup
import urllib.request
import requests

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
    print("Succesfully!")
else:
    print("Don't work")





