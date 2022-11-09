const http = require("http");
// C:\Users\andre\github_stuff\widgets.json
const data = require("C:\\Users\\andre\\github_stuff\\widgets.json")

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.writeHead(200, {"Content-Type": "text/json"});
    res.end(JSON.stringify(data));
  } 
  else if (req.url === "/widgB") {
    listNames(res);
  }
  else if (req.url === "/widg") {
    listBlue(res);
  }
  else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end("Data not found");
  }
});

const listBlue = (res) => {
  const colorBlue = data.filter((item) => {
    return item.color === "blue";
  });

  res.end(JSON.stringify(colorBlue));
}

const listNames = (res) => {
    const widgetNames = data.filter((item) => {
      return item.names === "names:";
    });
  
    res.end(JSON.stringify(widgetNames));
}

server.listen(3000);
console.log("Server is listening on port 3000");