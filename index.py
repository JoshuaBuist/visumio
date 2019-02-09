#!/usr/bin/env python

class Template:

    def __init__(self,url,_handles):

        self.url = url
        self.handles = _handles

    def render(self):
        
        page = "".join(open(self.url,'r').readlines())


def load_page(url):

    page = "".join(open(url,'r').readlines())

    values = [('value','Demo'),('value2','Hello World')]

    for i in range(2):
        page = page.format(values[i])

    return page


def render_page(content):

    print ('Content-type: text/html\n\n' + content)


# Main
#
def main():
    
    page = load_page("templates/app.html")
    render_page(page)

    main_page = Template('templates/app.html',[('value','Demo'),('value2','Hello World')])


if __name__ == "__main__":
    main() 