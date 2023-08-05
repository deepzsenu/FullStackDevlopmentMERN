const express = require("express");
const app = express();

const ExpressLayouts = require("express-ejs-layouts");

const port = 8000;

app.use(ExpressLayouts)
app.use('/', require("./routes"));

// app.use("/profile", require("./routes/user"));

// setup the view engine
app.set("view engine", "ejs");
app.set("views", "./views")

app.listen(port, (err) => {
    if (err) {
        // console.log("Error in connecting to server",err);
        console.log(`Error:${err}`);
        return;
    }
    console.log("Server connected successfully and running on port:", port);
})