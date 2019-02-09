#!/usr/bin/env python

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

    if "user" not in form:
        print("<h1>Not Logged In</h1")
        return

    # Initializes CGI page
    main_page = Page("Main").init()
   
    # Ensures page can be written to before template is loaded
    if main_page:
        main_content = Template('templates/app.html',{'value':form['user'].value,'value2':'Hello World'})
        main_content.render()


if __name__ == "__main__":
    main() # Starts main function