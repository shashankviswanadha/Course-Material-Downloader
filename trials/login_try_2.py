# -*- coding: utf-8 -*-
import cookielib, urllib, urllib2

# not the actual site, but still a Moodle example
theurl = 'http://www.mahindraecolecentrale.edu.in/portal/login/index.php'

username= '14xj00168'
password= 'Chester)&1'

passman = urllib2.HTTPPasswordMgrWithDefaultRealm()

passman.add_password(None, theurl, username, password)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPBasicAuthHandler(passman),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0),
    urllib2.HTTPCookieProcessor(cj),
)

urllib2.install_opener(opener)


# set headers
opener.addheaders = [
    ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                   'Windows NT 5.2; .NET CLR 1.1.4322)'))
]

try:
    #req = opener.open(theurl, data)
    req = opener.open(theurl)
except IOError, e:
    print "It looks like the username or password is wrong."

# == test ==

# visit "my courses":
req = opener.open("https://moodle.pucrs.br/my/‎")
content = ''.join(req.readlines())
print(content)
