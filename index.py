#!/usr/bin/env python3

def load_page(url):
    print ("".join(open(url,'r').readlines()))

def main():
    print ('Content-type: text/html\n\n')
    load_page("templates/app.html")

if __name__ == "__main__":
    main()