#!/usr/bin/env python3

# TO-DO 
# Proper authentification

import sys
import cgi
import cgitb

cgitb.enable() # Debug Setting

form = cgi.FieldStorage() # Data stored from POST

user = form.getvalue("user")
password = form.getvalue("pass")

print ('Content-Type: text/html\n\n')


if len(user) > 0 and len(password) > 5:
    print ('Location: http://http://68.183.200.39/index.py')
else:
    print ('Location: http://http://68.183.200.39/index.py?er=1')