import webapp2
import urllib2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class FbHandler(webapp2.RequestHandler):
	def get(self):
		access_token = self.request.get('access_token')
		
		if not access_token == '':
			self.redirect('../')

		code = self.request.get('code')
		
		if code == '':
			self.redirect('https://www.facebook.com/dialog/oauth?client_id=652896994869977&redirect_uri=https://sorteoiphone7.appspot.com/fb')
		else:
			response = urllib2.urlopen(str('https://graph.facebook.com/v2.7/oauth/access_token?client_id=652896994869977&redirect_uri=https://sorteoiphone7.appspot.com/fb&client_secret={app-secret}&code=' + code))
			html = response.read()
			self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/fb', FbHandler),
], debug=True)