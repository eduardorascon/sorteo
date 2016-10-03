from app_sorteo.default import DefaultHandler
from app_sorteo.facebook import FacebookHandler
import webapp2

app = webapp2.WSGIApplication([('/', DefaultHandler),
    ('/fb', FacebookHandler),], debug=True)