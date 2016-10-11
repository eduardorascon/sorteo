from app_sorteo.default import DefaultHandler
from app_sorteo.facebook import FacebookHandler
import webapp2

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([('/', DefaultHandler),
    ('/fb', FacebookHandler),], config=config, debug=True)