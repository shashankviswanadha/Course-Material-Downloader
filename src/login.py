import requests
from bs4 import BeautifulSoup
payload = {'username': '14xj00168', 'password': 'Chester)&1'}

with requests.Session() as c:
    c.post('http://www.mahindraecolecentrale.edu.in/portal/login/index.php', data=payload)
    r = c.get('http://www.mahindraecolecentrale.edu.in/portal/')
    data = r.content
    #print data
    soup = BeautifulSoup(data)
    links = soup.find_all("a")
    """for link in links:
        if link.get('href') != None:
            if 'http' in link.get('href'):
                print "<a href='%s'>%s</a>" %(link.get('href'),link.text)"""
    category_data = soup.find_all("div", {"class": "course_category_tree"})
    for item in category_data:
        for i in range(0,9):
            sub = item.contents[i].find_all("div", {"class": "category_label"})
            if len(sub) != 0:
                sem = sub[0]
                if len(sem) != 0:
                    if 'Semester' in sem.text:
                        var_name = ''.join(e for e in sem.text if e.isalnum())
                        #print var_name
                        exec("%s = %s" % (var_name,sem.get('href')))
    print SemesterI2015
