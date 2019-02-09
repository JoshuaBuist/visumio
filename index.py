#!/usr/bin/env python

def load_page(url,__handles = []):

    page = "".join(open(url,'r').readlines())

    page.format(VALUE="Hello World")
    
    #if len(__handles) > 0:
        # Added handles

    print (page)

def main():
    print ('Content-type: text/html\n\n')
    load_page("templates/app.html")

if __name__ == "__main__":
    main()