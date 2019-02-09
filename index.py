#!/usr/bin/env python

from string import Template

def load_page(url):

    page = "".join(open(url,'r').readlines()).format(value="TEST")

    Template(page).substitute(value="Hello World")

    print (page)

def main():
    print ('Content-type: text/html\n\n')
    load_page("templates/app.html")

if __name__ == "__main__":
    main() 