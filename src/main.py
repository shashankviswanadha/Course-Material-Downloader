# -*- coding: utf-8 -*-

def install(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
            import pip
            pip.main(['install', package])
install('requests')
install('bs4')
install('urllib2')
install('cookielib')
install('getpass')

import requests
from bs4 import BeautifulSoup
from custom_exceptions import *
from config import *
import urllib2
import cookielib
import sys
from utils import Login
import os
from getpass import getpass

def login(username, password, session):
    print "logging in user"
    payload = {'username': username, 'password': password}
    session.post('http://www.mahindraecolecentrale.edu.in/portal/login/index.php', data=payload)

def get_home_page(session):
    print 'retrieving home page'
    raw_home_page = session.get('http://www.mahindraecolecentrale.edu.in/portal/')
    home_page_data = raw_home_page.content
    if 'You are logged in as' in home_page_data:
        print 'logged in succesfully'
        return home_page_data
    else:
        raise LoginError("Your username or password is wrong")

def get_category_tree(home_page_data):
    soup = BeautifulSoup(home_page_data)
    category_data = soup.find_all("div", {"class": "course_category_tree"})
    return category_data

def get_semester_course_links(category_data):
    Semester = {}
    for item in category_data:
        for i in range(0,len(item.contents)):
            category = item.contents[i]
            sub_category = category.find_all("div", {"class": "category_label"})
            if len(sub_category) != 0:
                sem = sub_category[0]
                if len(sem) != 0:
                    if 'Semester' in sem.text:
                        var_name = ''.join(e for e in sem.text if e.isalnum())
                        course_link = category.find_all("a", {"class": "course_link"})
                        if course_link!= []:
                            Semester[var_name] = course_link

    for key,value in Semester.iteritems():
        lt = []
        del_sem = []
        d = {}
        for link in value:
            if 'Feedback' not in link.text:
                d[link.text] = link.get('href')
            else:
                Semester[key] = lt
                del_sem.append(key)
        Semester[key] = d
    for key in del_sem:
        del Semester[key]
    return Semester

def get_semester(sem_num,year,semester):
    roman_table = {1: 'I', 2: 'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII'}
    sem = 'Semester' + roman_table[sem_num] + str(year)
    if sem not in Semester:
        raise SemesterError("The year or semester number you enterd does not exist")
    return sem

def download_course(semester,course_name,pat,Semester,session):
    try:
        if pat[-1] == '/':
            pat = pat[:-1]
        path = pat
        print 'Downloading %s' %str(course_name.encode('utf8'))
        if not os.path.exists(path + '/' + 'Moodownloader'):
            os.makedirs(path + '/' + 'Moodownloader')
        path = path + '/' + 'Moodownloader' + '/'
        path = path + semester
        if not os.path.exists(path):
            os.makedirs(path)
        path = path + '/' + course_name
        if not os.path.exists(path):
            os.makedirs(path)
        path = path + '/'
        course_url = Semester[semester][course_name]
        request = session.get(course_url)
        links_soup = BeautifulSoup(request.content)
        raw = links_soup.find_all("a", {"class": ""})
        down = {}
        for x in raw:
            st = str(x)
            if 'powerpoint' in st:
                down[x.text + '.ppt'] = x.get('href')
            elif 'document' in st:
                down[x.text + '.docx'] = x.get('href')
            elif 'spreadsheet' in st:
                down[x.text + '.xml'] = x.get('href')
            else:
                down[x.text] = x.get('href')

        download_links = {}
        for name,link in down.iteritems():
            if 'mod/resource' in link:
                download_links[name] = link
        for name,link in download_links.iteritems():
            try:
                file_name = path + name
                if not os.path.isfile(file_name):
                    print '---------Downloading file %s ----------' %name
                    r = session.get(link)
                    f = open(file_name, 'wb')
                    for chunk in r.iter_content(chunk_size=512 * 1024):
                        if chunk: # filter out keep-alive new chunks
                            f.write(chunk)
                    f.close()
            except:
                raise FileError('Unable to understand file %s' %name)
    except:
        raise DownloadError('Could not download a file in %s' %course_name)
def download_all_courses(semester_name,Semester,session):
    count = 0
    for name,course_link in Semester[semester_name].iteritems():
        print 'Downloading course %d of %d' %(count+1,len(Semester[semester_name]))
        download_course(semester_name,name,Config.path,Semester,session)
        count += 1

if __name__ == '__main__':
    with requests.Session() as session:
        username = raw_input("Enter your moodle username:  ")
        password = getpass("Enter your password:  ")
        try:
            Login(username,str(password))
        except:
            pass
        login(username,password,session)
        home_page = get_home_page(session)
        category = get_category_tree(home_page)
        Semester = get_semester_course_links(category)
        sem_num = int(input('Enter the semester number:  '))
        year = int(input('Enter your year of joining:  '))
        sem = get_semester(sem_num,year,Semester)
        course = raw_input("Enter 'all' to download all courses in the semester or enter the precise course name to download only that course:  ")
        flag = 0
        if course == 'all':
            download_all_courses(sem,Semester,session)
        else:
            for key,value in Semester.iteritems():
                if course in value:
                    flag = 1
                    break
            if flag == 1:
                download_course(sem,course,Config.path,Semester,session)
            else:
                raise CourseNameError("Enter the precise course name as it appears on moodle")
