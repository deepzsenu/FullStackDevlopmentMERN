var http = require("http");

var port = 8080;

const fs = require("fs");

function requestHandler(req,res){
    console.log(req.url);
    res.writeHead(200, {"Content-Type": "text/html"});

    let filePath ;
    
    // using multiple file to render with different paths 
    switch(req.url){
        case '/':
            filePath = "./index.html";
            break;
        case '/profile':
            filePath = "./profile.html";
            break;
        default:
            filePath = "./404.html";
    }


    fs.readFile(filePath, function(err, data){
        if(err){
            console.log(err);
            return res.end("<h1>Error<h1>")
        }

        return res.end(data);
    })

    /*
    fs.readFile("./index.html", function(err,data){
        if(err){
            console.log("Error " , err);
            return res.end("<h1>Error found<h1>");
        }

        return res.end(data);
    });
    */

    // res.end("<h1> Server me!<h1>");
}

const server = http.createServer(requestHandler);

server.listen(port, function(err) {
    if (err) {
        console.log(err);
        return;
    }
    else{
        console.log("server is up at :", port);
        return
    }
})