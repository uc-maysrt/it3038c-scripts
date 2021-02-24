var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");
var server = http.createServer(function(req, res){
    if (req.url === "/"){
        fs.readFile("./public/index.html", "UTF-8", function(_err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
    })}
    else if(req.url.match("/sysinfo")){
    myHostName=os.hostname();
    html=`
        <!DOCTYPE html>
        <html>
            <head>
                <title>Node JS Response</title>
            </head>
            <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime: ${os.uptime()}</p>
                <!--https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat-->
                <p>Total Memory: ${Intl.NumberFormat().format(os.totalmem()/2048)} MB</p>
                <p>Free Memory: ${Intl.NumberFormat().format(os.freemem()/2048)} MB</p>
                <p>Number of CPUs: ${os.cpus().length}</p>
                <p>[This is actually kind of incorrect because of HyperThreading. It's a Quad core with 8 threads/logical cores]</p>
                <p> <a href="https://gist.github.com/brandon93s/a46fb07b0dd589dc34e987c33d775679">This would result in the correct answer.</a> </p>
            </body>
        </html>
    `
    res.writeHead(200, {"Content-Type":"text/html"})
    res.end(html);
    }
    else 
    {
    res.writeHead(404, {"Content-Type:":"text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
    }
});

server.listen(3000)
console.log("Server listening on port 3000")


/*Old, unused/changed below
    res.writeHead(200, {"Content-Type": "text/text"});
    res.end("Hello from Node")
    res.end(`
        <!DOCTYPE html>
            <head>
                <title>Node JS Response</title>
            </head>
            <body>
                <h1>Hello!</h1>
                <p>${req.url}</p>
                <p>${req.method}</p>
            </body>
        </html>
    `)
*/