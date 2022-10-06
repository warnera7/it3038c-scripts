
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
        html=`
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: </p>
            <p>Total Memory: </p>
            <p>Free Memory: </p>
            <p>Number of CPUs: </p>
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