#!/usr/bin/env python
import sys
import BaseHTTPServer
import SimpleHTTPServer

print sys.argv

def test(HandlerClass = SimpleAppServer,
          ServerClass = BaseHTTPServer.HTTPServer) :
    SimpleHTTPServer.test(HandlerClass, ServerClass)


html_body = """
<html><body>
foo = %s
</body></html>"""

import cgi
form = cgi.FieldStorage()
print "Content-type: text/html\n"
print html_body % (form.getvalue("id","N/A"))
