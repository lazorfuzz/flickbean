var vid = document.getElementById("bgvid");
var vidsources = document.getElementsById("vidsrc");

function gotoCoffee(){
	
	window.location='coffee.flick';
}

function putVideo(){

	vidID = randInt(1,5).toString();
	vidsrc[0].src = 'res/flickbean' + vidID + '.webm';
	vidsrc[1].src = 'res/flickbean' + vidID + '.mp4';
	vid.load();
	vid.play();
}

function randInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

vid.addEventListener('ended', function(){
	vid.pause();
}); 

