#!/usr/bin/env python3

import cgi
import cgitb
from src.app import Page, Template

# Main function
#
def main():

    cgitb.enable() # Debug Setting

    form = cgi.FieldStorage() # Data stored from POST

    # Initializes CGI page
    main_page = Page("Main").init()
   
    print(main_page)

    if 'error' not in main_page:
        if "user" not in form:

            msg = {'message':''}

            if "error" in form:
                msg['message'] = 'Error Code ' + str(form['error'].value + ": Incorrect username or password")

            login_content = Template('templates/login.html',msg)
            login_content.render()
        else:
            main_content = Template('templates/app.html',{'value':form['user'].value,'value2':form['auth'].value})
            main_content.render()


if __name__ == "__main__":
    main() # Starts main functionContent-type: text/html\n\n' # Returns false if error occurs