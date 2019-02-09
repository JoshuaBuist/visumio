#!/usr/bin/env python3

# TO-DO 
# Proper authentification

import sys
import cgi
import cgitb
from uuid import uuid4

cgitb.enable() # Debug Setting

form = cgi.FieldStorage() # Data stored from POST

user = form.getvalue("user")
password = form.getvalue("pass")
authToken = uuid4()

print ('Content-Type: text/html\r')


if len(user) > 0 and len(password) > 5:
    print ('Location: http://68.183.200.39/index.py?user=' + user +'&auth=' + authToken +'\r\n\r')
else:
    print ('Location: http://68.183.200.39/index.py?error=1\r\n\r')