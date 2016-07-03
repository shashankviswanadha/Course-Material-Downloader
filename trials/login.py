import requests
from bs4 import BeautifulSoup
with requests.Session() as c:
    url = 'http://www.mahindraecolecentrale.edu.in/portal/login/index.php'
    USERNAME = '14xj00168'
    PASSWORD = 'Chester)&1'
    c.get(url)
    csrf = c.cookies['csrftoken']
    login_data = dict(csrfmiddlewaretoken=csrf, username=USERNAME, password=PASSWORD,headers=dict(Referer=url), next='/')
    check = c.post(url,data=login_data)
    print check
    #print BeautifulSoup(requests.get(url).content)
    page = requests.get('http://www.mahindraecolecentrale.edu.in/portal/')
    r = page.content
    print r




    #soup = BeautifulSoup(r)
    #print soup.find_all("a")
    #print soup.prettify
