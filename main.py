import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class FbHandler(webapp2.RequestHandler):
	def get(self):
		code = self.request.get('code')
		if code == '':
			self.redirect('https://www.facebook.com/dialog/oauth?client_id=652896994869977&redirect_uri=https://sorteoiphone7.appspot.com/fb')
		else:
			self.response.write('code: ' + code)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/fb', FbHandler),
], debug=True)