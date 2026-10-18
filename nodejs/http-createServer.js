const http = require("http");

const server = http.createServer((req, res) => {
  console.log(req.url);
  if (req.url === "/") res.end("Hello\n");
  else {
    res.writeHead(404);
    res.end("Not found");
  }
});

server.listen(5002);
