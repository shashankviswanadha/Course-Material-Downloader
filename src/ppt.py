import requests
from bs4 import BeautifulSoup
import magic
payload = {'username': '14xj00168', 'password': 'Chester)&1'}

with requests.Session() as c:
    c.post('http://www.mahindraecolecentrale.edu.in/portal/login/index.php', data=payload)
    r = c.get('http://www.mahindraecolecentrale.edu.in/portal/')
    data = r.content
    #print data
    soup = BeautifulSoup(data)
    #links = soup.find_all("a")
    """for link in links:
        if link.get('href') != None:
            if 'http' in link.get('href'):
                print "<a href='%s'>%s</a>" %(link.get('href'),link.text)"""
    category_data = soup.find_all("div", {"class": "course_category_tree"})
    Semester = {}
    for item in category_data:
        for i in range(0,9):
            category = item.contents[i]
            sub = category.find_all("div", {"class": "category_label"})
            #print sub
            if len(sub) != 0:
                sem = sub[0]
                if len(sem) != 0:
                    if 'Semester' in sem.text:
                        var_name = ''.join(e for e in sem.text if e.isalnum())
                        t = category.find_all("a", {"class": "course_link"})
                        if t!= []:
                            Semester[var_name] = t

    for key,value in Semester.iteritems():
        lt = []
        for link in value:
            if 'Feedback' not in link.text:
                print link.text,'\n'
                lt.append(link.get('href'))
            else:
                Semester[key] = lt

    #print Semester
    rq = c.get(Semester['SemesterIV2014'][8])
    path = 'SemesterIV2014/OOP/'
    links_soup = BeautifulSoup(rq.content)
    raw = links_soup.find_all("a", {"class": ""})
    dow = {}
    for x in raw:
        st = str(x)
        if 'powerpoint' in st:
            dow[x.text + '.ppt'] = x.get('href')
        else:
            dow[x.text] = x.get('href')

    download_links = {}
    for name,link in dow.iteritems():
        if 'mod/resource' in link:
            download_links[name] = link
    #print download_links,len(download_links)
    #urllib.urlretrieve(download_links[0],'yeah.html')
    print download_links
    ppts = {}
    for name,link in download_links.iteritems():
        try:
            r = c.get(link)
            f_name = path + name
            f = open(f_name, 'wb')
            for chunk in r.iter_content(chunk_size=512 * 1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        except:
            print name
            ppts[name] = link
    f.close()
    for name,link in ppts.iteritems():
        try:
            f_name = name+'.ppt'
            f = open(f_name, 'wb')
            for chunk in r.iter_content(chunk_size=512 * 1024):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        except:
            print name
        f.close()
    """r = c.get('http://www.mahindraecolecentrale.edu.in/portal/mod/resource/view.php?id=1127')
    f = open('', 'wb')
    for chunk in r.iter_content(chunk_size=512 * 1024):
        if chunk: # filter out keep-alive new chunks
            f.write(chunk)
    f.close()"""
