function buildOrder(el){
	var beantype = el.children[0].innerText.split('\n')[0];
	alert(beantype);
	window.location = 'http://apolyse.com/cgi-bin/flickbean/buildorder?bean=' + beantype.replace(' ', '+');
}