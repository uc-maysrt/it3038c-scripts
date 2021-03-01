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
                    <style>
                    p{
                        padding-left: 60px;
                    }
                    </style>
                </head>
                <body>
                    <br />
                    <p style="">Hostname: ${myHostName}</p>
                    <p>IP: ${ip.address()}</p>
                    <p>Server Uptime: ${timeToString(os.uptime())}</p>
                    <!--https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat for those precious commas-->
                    <p>Total Memory: ${Intl.NumberFormat().format(os.totalmem() / 1024 / 1024)} MB</p>
                    <p>Free Memory: ${Intl.NumberFormat().format(os.freemem() / 1024 / 1024)} MB</p>
                    <p>Number of CPUs: ${os.cpus().length} (see HTML comment below)</p>
                    <!--This is actually kind of incorrect on my PC because of HyperThreading. I have a Quad core (physical cores) with 8 threads/logical cores (4C/8T).
                    https://gist.github.com/brandon93s/a46fb07b0dd589dc34e987c33d775679 would result in the correct answer.
                    It also gets murky because it depends on model number/generation.
                    An Intel i7/i9 will have Hyperthreading, an i3 would not, and i5s both have and have not, depending on model number.
                    Apparently Intel added hyperthreading to i3s and i5s in 2019 and sometimes the mobile i5s had it in the past.
                    This also applies to AMD CPUs, they just call it something else (SMT) because trademarks and such.
                    Rather than install that though, I just divided it in half.
                    -->
                    <p>Actual number of CPUs: ${os.cpus().length / 2}</p>
                    <br />
                    <br />
                </body>
            </html>
        `
        res.writeHead(200, {"Content-Type":"text/html"})
        res.end(html);
        }
    else {
        res.writeHead(404, {'content-type': 'text/html'})
        res.end(`404 File Not Found at ${req.url}`)
        }
});
server.listen(3000);
console.log("Server listening on port 3000");