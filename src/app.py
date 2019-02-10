#!/usr/bin/env python3

import cgi
import cgitb

class Page:

    def __init__(self,_name):
        self.name = _name


    def init(self):

        # Tests if cgi can write to browser
        try:
            return 'Content-type: text/html\n\n'
        except:
            return 'error0'


class Template:

    templates = list()

    def __init__(self,_url,_handles):

        self.url = _url
        self.handles = _handles

    def render(self):
        
        # Renders page with preset template handles
        self.content = "".join(open(self.url,'r').readlines()) # Removes trailing '\n'
        self.content = self.content.format(**self.handles)
        
        print(self.content)