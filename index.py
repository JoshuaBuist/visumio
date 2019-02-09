#!/usr/bin/env python

class Page:

    def __init__(self,_name):
        self.name = _name


    def init(self):

        # Tests if cgi can write to browser
        #
        try:
            print('Content-type: text/html\n\n')
            return True
        except:
            return False


class Template:

    def __init__(self,_url,_handles):

        self.url = _url
        self.handles = _handles


    def render(self):
        
        self.content = "".join(open(self.url,'r').readlines())
        self.content = self.content.format(**self.handles)
        
        print(self.content)


def load_page(url):

    page = "".join(open(url,'r').readlines())

    values = {'value':'Demo','value2':'Hello World'}

    page = page.format(**values)

    return page


def render_page(content):

    print ('Content-type: text/html\n\n' + content)


# Main
#
def main():
    
    #page = load_page("templates/app.html")
    #render_page(page)

    main_page = Page("Main").init()

    if main_page:
        main_content = Template('templates/app.html',{'value':'Demo','value2':'Hello World'})
        main_content.render()



if __name__ == "__main__":
    main() 