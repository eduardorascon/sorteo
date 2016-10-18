import webapp2
import urllib2
import stripe
import base

class PaymentsHandler(base.BaseHandler):
	#this key needs to change when released.
	stripe.api_key = 'sk_test_IHNilUCltlHhK0M4NZFV8Z1i'

	def post(self):
		token = self.request.get('stripeToken')
		ticket =  self.request.get('ticket')
		self.response.write('token: ' + token + '<br />')

		try:
			charge = stripe.Charge.create(
				amount = 4900 if token == 'B' else 7900,
				currency = "MXN",
				source = token,
				description = "Example charge"
			)
		except stripe.error.CardError as e:
			self.response.write('error: ' + e)
			pass