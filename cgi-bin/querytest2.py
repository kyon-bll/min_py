#!/usr/bin/env python
# coding: utf-8

import cgi
form=cgi.FieldStorage()

html_body = u"""
<html>
<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
</head>
<body>
<form action = "/cgi-bin/querytest2.py" method="POST">
%s
<input type="submit" />
</form>
%s
</body>
</html>"""

checkboxs = ""
content = ""

languages = ["Python", "Ruby", "Perl", "PHP"]

for l in languages:
    checkboxs += '<input type = "checkbox" name = "language" value = %s />%s<br />' % (l, l)

lang = form.getlist("language")
    
if lang:
    for cnt, item in enumerate(lang):
        content += "%d : %s <br />" % (cnt+1, item)

print "Content-type: text/html;charset=utf-8\n"
print (html_body % (checkboxs, content)).encode("utf-8")
