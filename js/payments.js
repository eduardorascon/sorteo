var handler = StripeCheckout.configure({
	//this key needs to change when released.
	key: 'pk_test_8dd3LPVANWkLgE2WDXIcXLfw',
	locale: 'auto',
	currency: 'MXN',
	zipCode: true,
	//billingAddress: true,
	name: 'Sorteo iPhone 7'
	//panelLabel: '¡Comprar!',
});

window.onload = function(){
	var firstButton = document.getElementById('firstButton');
	firstButton.addEventListener('click', function(e){
		handler.open({
			description: 'Boleto básico',
			amount: 4900,
			token: function(token) {
				paymentsPost({stripeToken: token.id, ticketType: 'B'})
			}
		});
		e.preventDefault();
	});

	var secondButton = document.getElementById('secondButton');
	secondButton.addEventListener('click', function(e){
		handler.open({
			description: 'Boleto PREMIUM',
			amount: 7900,
			token: function(token) {
				paymentsPost({stripeToken: token.id, ticketType: 'P'});
			}
		});
		e.preventDefault();
	});
}

window.addEventListener('popstate', function(){
	handler.close();
})

function paymentsPost(params){
	var form = document.createElement('form');
	form.setAttribute('method', 'post');
	form.setAttribute('action', '/payments');

	for(var key in params){
		if(params.hasOwnProperty(key)){
			var hiddenField = document.createElement('input');
			hiddenField.setAttribute('type', 'hidden');
			hiddenField.setAttribute('name', key);
			hiddenField.setAttribute('value', params[key]);
			form.appendChild(hiddenField);
		}
	}

	document.body.appendChild(form);
	form.submit();
}