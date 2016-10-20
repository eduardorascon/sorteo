from app_sorteo.default import DefaultHandler
from app_sorteo.facebook import FacebookHandler
from app_sorteo.payments import PaymentsHandler
import webapp2

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key' : 'my-super-secret-key',
    'backends' : { 'datastore' : 'webapp2_extras.appengine.sessions_ndb.DatastoreSessionFactory'}
}

app = webapp2.WSGIApplication([
	('/', DefaultHandler),
	('/fb', FacebookHandler),
	('/payments', PaymentsHandler)],
config=config, debug=True)