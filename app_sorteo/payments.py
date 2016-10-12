import webapp2
import urllib2
import stripe
import base

class PaymentsHandler(base.BaseHandler):
	#this key needs to change when released.
	stripe.api_key = 'pk_test_8dd3LPVANWkLgE2WDXIcXLfw'
	def post(self):
		token = self.request.get('stripeToken')
		self.response.write('token: ' + token)