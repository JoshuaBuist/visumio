#!/usr/bin/env python

def load_page(url):
    page = "".join(open(url,'r').readlines())
    print (page)

def main():
    print ('Content-type: text/html\n\n')
    load_page("templates/app.html")

if __name__ == "__main__":
    main()