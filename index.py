#!/usr/bin/env python

print ('Content-type: text/html\n\n')

def load_page(url):

    page = "".join(open(url,'r').readlines())

    print (page)

def main():
    load_page("templates/app.html")

if __name__ == "__main__":
    main()