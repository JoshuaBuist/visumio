#!/usr/bin/env python3

import cgi
import cgitb

class Page:

    def __init__(self,_name):
        self.name = _name


    def init(self):

        # Tests if cgi can write to browser
        try:
            print('Content-type: text/html\n\n')
            return True
        except:
            return False # Returns false if error occurs


class Template:

    def __init__(self,_url,_handles):

        self.url = _url
        self.handles = _handles


    def render(self):
        
        # Renders page with preset template handles
        self.content = "".join(open(self.url,'r').readlines()) # Removes trailing '\n'
        self.content = self.content.format(**self.handles)
        
        print(self.content)


# Main function
#
def main():

    cgitb.enable() # Debug Setting

    form = cgi.FieldStorage() # Data stored from POST

    # Initializes CGI page
    main_page = Page("Main").init()
   
    if main_page:
        if "user" not in form:

            msg = {'message':''}

            if "error" in form:
                msg['message'] = 'Error Code ' + str(form['error'].value + ": Incorrect username or password")

            login_content = Template('templates/login.html',msg)
            login_content.render()
        else:
            main_content = Template('templates/app.html',{'value':form['user'].value,'value2':form['svpp'].value})
            main_content.render()


if __name__ == "__main__":
    main() # Starts main function