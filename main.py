import webapp2
import app

app = webapp2.WSGIApplication([('/', DefaultHandler),
    ('/fb', FbHandler),], debug=True)