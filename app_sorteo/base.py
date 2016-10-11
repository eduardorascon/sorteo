import webapp2
from webapp2_extras import sessions

class BaseHandler(webapp2.RequestHandler):
	def dispatch(self):
		#Get a session store for this request.
		self.session_store = sessions.get_store(request = self.request)

		try:
			#Dispatch the request.
			webapp2.RequestHandler.dispatch(self)
		finally:
			#Save all sessions.
			self.session_store.save_sessions(self.response)

	@webapp2.cached_property
	def session(self):
		#Returns a session using the datastore backend.
		return self.session_store.get_session(backend = 'datastore')

#sources
#http://www.essentialtech.co.nz/content/using_session_google_app_engine_and_python_27
#http://aspiringpythoness.blogspot.mx/2012/01/how-to-configure-different-session.html