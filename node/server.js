
const fs = require("fs");
const http = require("http");
const os = require("os");
const ip = require('ip')

http.createServer((req, res) => {
    if (req.url === "/") {
        fs.readFile(`${__dirname}\\Public\\index.html`, "UTF-8", (err, body) => {
            if (err) { throw (err) }
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    
    } else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        serverUptime=os.uptime();
        //this was super fun to get working correctly, based off the comment by Christian Meyer at https://stackoverflow.com/questions/13903897/javascript-return-number-of-days-hours-minutes-seconds-between-two-dates
        dayUptime = (serverUptime / 86400);
        hourUptime = (dayUptime % 1) * (24);
        minuteUptime = (hourUptime % 1) * (60);
        secondsUptime = (minuteUptime % 1) * (60);
        //testUptime = [Math.floor(serverUptime), Math.floor(dayUptime), Math.floor(hourUptime), Math.floor(minuteUptime), Math.floor(secondsUptime)];

        totalMem=os.totalmem();
        totalMBMem = (totalMem / 1000000).toFixed(2);
        freeMem=os.freemem();
        freeMBMem = (freeMem / 1000000).toFixed(2);

        CPUdata=os.cpus().length;
        
        html=`
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${Math.floor(dayUptime)}, Hours: ${Math.floor(hourUptime)}, Minutes: ${Math.floor(minuteUptime)}, Seconds: ${secondsUptime.toFixed(0)}</p>
            <p>Total Memory: ${totalMBMem} MB</p>
            <p>Free Memory: ${freeMBMem} MB</p>
            <p>Number of CPUs: ${CPUdata}</p>
          </body>
        </html>`
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html); 
    
    }  else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File not found at ${req.url}`);
    }
    
}).listen(3000);

console.log("Server listening on port 3000")

// const server = http.createServer((req, res) => {
    
//     res.writeHead(200, {"Content-Type": "text/html"});

//     res.end(`
//         <!DOCTYPE html>
//         <html>
//             <head>
//                 <title>Node JS Response</title>
//             </head>
//             <body>
//                 <h1>Hello!</h1>
//                 <p>${req.url}</p>
//                 <p>${req.method}</p>
//             </body>
//         </html>
//     `)
// }).listen(3000)

// console.log("server listening on port 3000")