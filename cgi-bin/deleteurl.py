#!/usr/bin/env python
# coding: utf-8

from simpletemplate import SimpleTemplate
from rssurl import Rssurl
from os import path
from httphandler import Request, Response
import cgitb;cgitb.enable()

value_dic = {'errors':"", 'title':'', 'url':'', 'item_id':''}

req = Request()
f = req.form

p = path.join(path.dirname(__file__), 'deleteform.html')

id = f.getvalue("id")
rss = Rssurl(id=int(id))

if not f.getvalue('posted'):
    id = f.getvalue('id')
    rss = Rssurl(id=int(id))
    value_dic.update({'title':rss.title, 'url':rss.url, 'item_id':id})
else:
    id = f.getvalue('id')
    rss = Rssurl(id=int(f.getvalue('id')))
    rss.delete()
    p = path.join(path.dirname(__file__), "posted.html")
    value_dic["message"] = u"RSS取得URLをさくじょしたお！"

t = SimpleTemplate(file_path = p)
res = Response()
body = t.render(value_dic)
res.set_body(body)
print res
