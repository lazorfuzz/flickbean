function buildOrder(el, formtype){
	var beantype = el.children[0].innerText.split('\n')[0];
    var form = document.createElement('form');
    form.setAttribute('method', 'post');
    form.setAttribute("action", 'buildorder.flick');
    var typeField = document.createElement("input");
    typeField.setAttribute("type", "hidden");
    typeField.setAttribute("name", "formtype"); 
    typeField.setAttribute("value", formtype);
    form.appendChild(typeField);
    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name", "bean"); 
    hiddenField.setAttribute("value", beantype);
    form.appendChild(hiddenField);
    document.body.appendChild(form);
    form.submit();
}

function submitCart(checkout){
	var beantype = document.getElementById('bean');
	var roasttype = document.getElementById('roasttype');
	var amount = document.getElementById('amount');
	var grinded = document.getElementById('grinded');
	var packaging = document.getElementById('packaging');
	var instructions = document.getElementById('instructions');

	inputs = [beantype, roasttype, amount, grinded, packaging, instructions];
	if (checkout == true){
		var checkField = document.createElement('input');
		checkField.setAttribute('type', 'hidden');
		checkField.setAttribute('name', 'checkout');
		checkField.setAttribute('id', 'checkout');
		checkField.setAttribute('value', 'were checking out baby :D');
		document.body.appendChild(checkField);
		inputs.push(document.getElementById('checkout'));
	}
	var form = document.createElement('form');
	form.setAttribute('method', 'post');
	form.setAttribute('action', 'buildorder.flick');

	for (i=0; i < inputs.length; i++){
		var typeField = document.createElement('input');
		typeField.setAttribute('type', 'hidden');
		typeField.setAttribute('name', inputs[i].id);
		typeField.setAttribute('value', inputs[i].value);
		form.appendChild(typeField);
	}
	document.body.appendChild(form);
	form.submit();
}

function deleteOrder(el, redirect){
	var form = document.createElement('form');
	form.setAttribute('method', 'post');
	form.setAttribute('action', 'buildorder.flick');
	var field = document.createElement('input');
	field.setAttribute('type', 'hidden');
	field.setAttribute('name', 'deleteorder');
	field.setAttribute('value', el.id);
	form.appendChild(field);
	var redr_field = document.createElement('input');
	redr_field.setAttribute('type', 'hidden');
	redr_field.setAttribute('name', 'delredr');
	redr_field.setAttribute('value', redirect);
	form.appendChild(redr_field);
	document.body.appendChild(form);
	form.submit();
}

function modOrder(el){
	var form = document.createElement('form');
	form.setAttribute('method', 'post');
	form.setAttribute('action', 'buildorder.flick');
	var field = document.createElement('input');
	field.setAttribute('type', 'hidden');
	field.setAttribute('name', 'modorder');
	field.setAttribute('value', el.id);
	form.appendChild(field);
	document.body.appendChild(form);
	form.submit();
}

function submitCheckout(){
	submitCart(true);

}

function submitShipping(){
	var inputs = document.forms["shipping"].getElementsByTagName("input");
	for (i = 0; i < inputs.length; i++){
		if (inputs[i].value.length < 2){
			alert('Please fill out the form.');
			return;
		}
	}
	document.forms["shipping"].submit();
	document.getElementsByName('shippingcontainer').style = 'display:none;'
}

function submitContact(){
	var inputs = document.forms["contact"].getElementsByTagName("input");
	for (i = 0; i < inputs.length; i++){
		if (inputs[i].value.length < 1 || document.getElementById('message').value.length < 1){
			alert('Please fill out the form.');
			return;
			}
		if (!inputs[0].value.includes('@')){
			alert('Please enter a valid email.');
			return;
			}
		}
		document.getElementById('contact').submit();
	document.getElementById('confirmation').style = 'display:block; color: rgba(102, 255, 102, 0.7); text-align:center;';
	document.getElementById('contactbutton').style='display:none;';
}

function inArray(value, array) {
  return array.indexOf(value) > -1;
}

function initBuildPage(){
	displaySelection('light');
	displaySelection('12');
	displaySelection('paper');
	displaySelection('yes');
}

function displaySelection(elId){
	selectStyle = 'background: rgba(102, 255, 102, 0.6);box-shadow: inset 0px 0px 8px rgba(0,0,0,0.5);';
	unselectStyle = 'background: rgba(255,255,255,0.23); box-shadow: none;';
	rTypes = ['light', 'medium', 'dark'];
	amounts = ['12', '24', '36'];
	packages = ['paper', 'plastic', 'jar'];
	grinded = ['yes', 'no'];
	document.getElementById(elId).setAttribute('style', selectStyle);
	if (inArray(elId, rTypes)){
		for (var i = 0; i < rTypes.length; i++){
			if (elId != rTypes[i]){
				document.getElementById(rTypes[i]).setAttribute('style', unselectStyle);
			}
		}
		document.getElementById('finalroasttype').innerText = 'Roast: ' + elId;
	}
	if (inArray(elId, amounts)){
		for (var i = 0; i < amounts.length; i++){
			if (elId != amounts[i]){
				document.getElementById(amounts[i]).setAttribute('style', unselectStyle);
			}
		}
		document.getElementById('finalamount').innerText = 'Amount: ' + elId + ' Oz.';
	}
	if (inArray(elId, packages)){
		for (var i = 0; i < packages.length; i++){
			if (elId != packages[i]){
				document.getElementById(packages[i]).setAttribute('style', unselectStyle);
			}
		}
		document.getElementById('finalpackage').innerText = 'Packaging: ' + elId;
	}
	if (inArray(elId, grinded)){
		for (var i = 0; i < grinded.length; i++){
			if (elId != grinded[i]){
				document.getElementById(grinded[i]).setAttribute('style', unselectStyle);
			}
		}
		document.getElementById('finalgrinded').innerText = 'Grinded: ' + elId;
	}

}

function setRoastType(roastType){
	displaySelection(roastType);
	document.getElementById('roasttype').value = roastType;
}

function setAmount(amount){
	displaySelection(amount);
	document.getElementById('amount').value = amount;
}

function setPackage(pack){
	displaySelection(pack);
	document.getElementById('packaging').value = pack;
}

function setGrinded(choice){
	displaySelection(choice);
	document.getElementById('grinded').value = choice;
}

function displayInstructions(){
	document.getElementById('finalinstructions').innerText = 'Additional Instructions: ' + document.getElementById('instructions').value;
}