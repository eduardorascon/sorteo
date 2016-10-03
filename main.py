import webapp2
import app

app = webapp2.WSGIApplication([('/', MainHandler),
    ('/fb', FbHandler),], debug=True)