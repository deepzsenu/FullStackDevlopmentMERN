const express = require("express");
const path = require("path");

const port = 8085;
const db = require("./config/mongoose.js");

const Task = require("./models/task.js");

const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

app.use(express.urlencoded())

app.use(express.static('assets'));


app.listen(port, (err) => {
    if (err) {
        console.log(`Error : ${err}`);
        return;
    }
    console.log(`Server is up and running at post: ${port}`);
})