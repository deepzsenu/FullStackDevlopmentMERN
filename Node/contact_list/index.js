const express = require("express");
const path = require("path");   

const port = 8080;
const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.get("/", (req, res)=>{
    console.log(__dirname);
    // res.send("<h1>Cool it is running.<h1>");
    return res.render("home", {title :"contact list"})
})
app.get("/contacts", (req,res)=>{
    return res.render("contacts", {title:"contact list"})
})

app.listen(port, function(err) {
    if (err) {
        console.log("you got an Error\n",err);
    }
    console.log("Server ready at Port", port);
})