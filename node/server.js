var fs = require("fs");
var http = require("http");
var os = require("os");
var ip = require("ip");
function timeToString(seconds)
{
    // https://www.neowin.net/forum/topic/817666-javascriptconvert-seconds-to-days-hours-minutes-and-seconds/
    var dayscount = Math.floor(seconds / 864000)
    var hourscount = Math.floor((seconds % 86400) / 3600)
    var minutescount = Math.floor(((seconds % 86400) % 3600) / 60)
    var secondscount = ((seconds % 86400) % 3600) % 60
    return dayscount + "days, " + hourscount + "hours, " + minutescount + "minutes, " + secondscount + "seconds"
}

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
                <p>Server Uptime (seconds): ${os.uptime()}</p>
                <p>Server Uptime: ${timeToString(os.uptime())}</p>
                <!--https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat for those precious commas-->
                <p>Total Memory: ${Intl.NumberFormat().format(os.totalmem() / 1024 / 1024)} MB</p>
                <p>Free Memory: ${Intl.NumberFormat().format(os.freemem() / 1024 / 1024)} MB</p>
                <p>Number of CPUs: ${os.cpus().length}</p>
                <p>Actual number of CPUs: ${os.cpus().length / 2}</p>
                <p>[This is actually kind of incorrect because of HyperThreading. It's a Quad core with 8 threads/logical cores]</p>
                <p> <a href="https://gist.github.com/brandon93s/a46fb07b0dd589dc34e987c33d775679">This would result in the correct answer.</a> </p>
                <p>Rather than install that though, I just divided it in half</p>
                <p>This also applies to AMD CPUs, they just call it something else because trademarks and such.</p>

            </body>
        </html>
    `
    res.writeHead(200, {"Content-Type":"text/html"})
    res.end(html);
    }
/*This seemed to cause me to get a "ERR_INVALID_HTTP_TOKEN" error everytime in "x:9" which would be the res.writeHead part
   else {
    res.writeHead(404, {"Content-Type:": "text/plain"});
    res.end(`404 File not Found at ${req.url}`);
    }*/
});
server.listen(3000);
console.log("Server listening on port 3000");