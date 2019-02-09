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

print ('Content-Type: text/html\r')


if len(user) > 0 and len(password) > 5:
    print ('Location: http://68.183.200.39/index.py\r\n\r')
else:
    print ('Location: http://68.183.200.39/index.py?error=1\r\n\r')