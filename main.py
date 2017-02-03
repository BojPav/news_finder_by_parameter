#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import jinja2
import webapp2
import urllib2
import webbrowser

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")


class PretragaHandler(BaseHandler):
    def post(self):

        trazeni_pojam = self.request.get("trazeni_pojam")

        delo = urllib2.urlopen("http://www.delo.si/svet")
        dnevnik = urllib2.urlopen("https://www.dnevnik.si/svet")

        rtvslo = urllib2.urlopen("http://www.rtvslo.si/svet/")
        siol = urllib2.urlopen("http://siol.net/novice/svet")
        ur24 = urllib2.urlopen("http://www.24ur.com/novice/svet/")


        delo_text = delo.read()
        dnevnik_text = dnevnik.read()

        rtvslo_text = rtvslo.read()
        siol_text = siol.read()
        ur24_text = ur24.read()

        sajtovi = []

        result = "Nije pronadjena nijedna vest za zadati pojam..."

        params = {"result": result,"sajtovi": sajtovi}

        if trazeni_pojam in delo_text:
            sajtovi.append("http://www.delo.si/svet")

        if trazeni_pojam in dnevnik_text:
            sajtovi.append("https://www.dnevnik.si/svet")

        if trazeni_pojam in rtvslo_text:
            sajtovi.append("http://www.rtvslo.si/svet/")

        if trazeni_pojam in siol_text:
            sajtovi.append("http://siol.net/novice/svet")

        if trazeni_pojam in ur24_text:
            sajtovi.append("http://www.24ur.com/novice/svet/")

        #else:
            #return self.render_template("hello.html", params=params)
        if len(sajtovi) < 1:
            return self.write("Nijedan sajt ne sadrzi zadati pojam")

        return self.render_template("pretraga.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/pretraga', PretragaHandler),
], debug=True)

