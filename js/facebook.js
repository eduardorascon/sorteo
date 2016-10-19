window.onload = function(){
	var dialog = document.querySelector('dialog');
	var showDialogButton = document.querySelector('#fbLoginButton');
	if (! dialog.showModal) {
		dialogPolyfill.registerDialog(dialog);
	}
	
	showDialogButton.addEventListener('click', function() {
		dialog.showModal();
	});
	
	dialog.querySelector('.close').addEventListener('click', function() {
		dialog.close();
	});

	var fbPostButton = document.querySelector('#fbPostButton');
	fbPostButton.addEventListener('click', function(){
		document.forms['hiddenForm'].submit();
	});
}