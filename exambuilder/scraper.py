import cookielib
import urllib2
import mechanize
import re
from defaults import *

# Browser
br = mechanize.Browser()

# Enable cookie support for urllib2
cookiejar = cookielib.LWPCookieJar()
br.set_cookiejar(cookiejar)

# Broser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# ??
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=5)

br.addheaders = [('User-agent',
                'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# authenticate



def auth(email, password):
    br.open(loginaddress)
    br.select_form(name="loginForm")

    br["email"] = email
    br["password"] = password
    res = br.submit()
    return res



res = auth(email, password)

# Now we should be logged in - go to the page for 2016-2009 papers, all Communication, and read in the raw HTML
page = br.open(
    paperaddress)
rawhtml = page.read().decode("UTF-8")

# split the raw line into a list, one line of html per list item.
htmllines = rawhtml.splitlines()
pattern = re.compile("\(.*-Paper.*\)")



def processHTML(htmllines, pattern):

    # Check line by line to see if it contains the paper number.
    papers = []
    for line in htmllines:
        if pattern.findall(line):
            # echo out the line number
            papers.append(line)
        # check if it's a question image link and echo

        # check if it's an answer image link and echo
    return papers


# TODO: Find the total number of questions, iterate over that. cjr

papers = processHTML(htmllines, pattern)

print papers
print rawhtml
