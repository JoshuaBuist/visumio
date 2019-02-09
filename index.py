#!/usr/bin/env python

class Template:

    def __init__(self,_view,_handles):
        self.view = _view
        self.handles = _handles

    def render(self):
        print (self.view)


def load_page(url):

    page = str(open(url,'r').readlines())

    return page


def render_page(content):

    print ('Content-type: text/html\n\n' + content)


# Main
#
def main():
    
    page = load_page("templates/app.html")
    render_page(page)

    main_page = Template('templates/app.html',['value','value2'])


if __name__ == "__main__":
    main() 