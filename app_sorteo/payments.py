import webapp2
import urllib2
import stripe
import base

class PaymentsHandler(base.BaseHandler):
	#this key needs to change when released.
	stripe.api_key = 'sk_test_IHNilUCltlHhK0M4NZFV8Z1i'
	def post(self):
		token = self.request.get('stripeToken')
		self.response.write('token: ' + token.id + '<br />')

		try:
			charge = stripe.Charge.create(
				amount = 1000,
				currency = "MXN",
				source = token.id,
				descripcion = "Example charge"
			)
		except stripe.error.CardError as e:
			self.response.write('error: ' + e)
			pass