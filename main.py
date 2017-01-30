#!/usr/bin/env python
import os
import jinja2
import webapp2
import requests
import webbrowser
#   from BeautifulSoup import BeautifulSoup

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
    def post(self):

        trazeni_pojam = self.request.get("trazeni_pojam")

        delo = requests.get("http://www.delo.si/svet")
        dnevnik = requests.get("https://www.dnevnik.si/svet")
        vecer = requests.get("http://www.vecer.com/rubrika/svet")
        rtvslo = requests.get("http://www.rtvslo.si/svet/")
        siol = requests.get("http://siol.net/novice/svet")
        ur24 = requests.get("http://www.24ur.com/novice/svet/")

        #trazeni_pojam = raw_input("Upisite pojam---> ")

        if trazeni_pojam in delo.text:
            print "Pronadjen pojam..."
            print "Otvaram DELO.SI..."
            webbrowser.open("http://www.delo.si/svet")

        if trazeni_pojam in dnevnik.text:
            print "Pronadjen pojam..."
            print "Otvaram DNEVNIK.SI..."
            webbrowser.open("https://www.dnevnik.si/svet")

        if trazeni_pojam in vecer.text:
            print "Pronadjen pojam..."
            print "Otvaram VECER.COM..."
            webbrowser.open("http://www.vecer.com/rubrika/svet")

        if trazeni_pojam in rtvslo.text:
            print "Pronadjen pojam..."
            print "Otvaram RTV.SLO..."
            webbrowser.open("http://www.rtvslo.si/svet/")

        if trazeni_pojam in siol.text:
            print "Pronadjen pojam..."
            print "Otvaram SIOL.NET..."
            webbrowser.open("http://siol.net/novice/svet")

        if trazeni_pojam in ur24.text:
            print "Pronadjen pojam..."
            print "Otvaram 24UR.COM..."
            webbrowser.open("http://www.24ur.com/novice/svet/")

        else:
            print "nema trazenih pojmova..."

        print "Provera zavrsena"


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
