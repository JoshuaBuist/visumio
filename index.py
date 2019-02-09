#!/usr/bin/env python

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
    
    # Initializes CGI page
    main_page = Page("Main").init()
   
    # Ensures page can be written to before template is loaded
    if main_page:
        main_content = Template('templates/app.html',{'value':'Debug','value2':'Hello World'})
        main_content.render()

        main_content.handles['value2'] = "Actually Goodbye"


if __name__ == "__main__":
    main() 