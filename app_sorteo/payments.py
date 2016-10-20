# -*- coding: utf-8 -*-
import webapp2
import urllib2
import stripe
import base

class PaymentsHandler(base.BaseHandler):
	#this key needs to change when released.
	stripe.api_key = 'sk_test_IHNilUCltlHhK0M4NZFV8Z1i'

	def post(self):
		#Check if user is logged in
		if self.session.get('access_token') == None:
			raise ValueError('Usuario no válido')

		#We need to make get the correct charge amount.
		ticketType =  self.request.get('ticketType')
		if ticketType not in 'BP':
			raise ValueError('Boleto no disponible.')

		amount = 4900 if ticketType == 'B' else 7900,

		token = self.request.get('stripeToken')
		self.response.write('token: ' + token + '<br />')

		try:
			charge = stripe.Charge.create(
				amount = amount,
				currency = "MXN",
				source = token,
				description = "Example charge"
			)
		except stripe.error.CardError as e:
			self.response.write('error: ' + e)
			pass