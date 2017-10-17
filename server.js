var http = require('http');
var cp = require('child_process');

var rgbbb = [];
var mario = 8080

var eggy = /^\/party(\d+)/
var reggy = /^\/partyEnd(\d+)/

function handler(req, res) {
	res.end("hello world");
	console.log("noe skjedde!", req.method, req.url);

	if (req.method == "POST" && eggy.test(req.url) && rgbbb[req.url.match(eggy)[1]] == null) {
		var lightOn = req.url.match(eggy)[1];
		console.log(lightOn);
		rgbbb[lightOn] = cp.spawn("python", ["rgbbb.py", lightOn]);
		rgbbb[lightOn].stdout.pipe(process.stdout);
		rgbbb[lightOn].stderr.pipe(process.stderr);
	}
	else if (req.method == "POST" && reggy.test(req.url) && rgbbb[req.url.match(reggy)[1]] != null) {
		var lightOn = req.url.match(reggy)[1];
		console.log(lightOn);
		rgbbb[lightOn].kill();
		rgbbb[lightOn] = null;
	}
}

var server = http.createServer(handler);
server.listen(mario);
console.log("itsa me,", mario);
