var vid = document.getElementById("bgvid");

function gotoCoffee(){
	window.location='coffee.html';
}

vid.addEventListener('ended', function(){
	vid.pause();
}); 

