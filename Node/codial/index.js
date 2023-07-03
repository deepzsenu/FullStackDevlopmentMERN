const express = require("express");
const app = express();
const port = 8000;

app.use('/', require("./routes"));

app.listen(port, (err) => {
    if (err) {
        // console.log("Error in connecting to server",err);
        console.log(`Error:${err}`);
        return;
    }
    console.log("Server connected successfully and running on port:", port);
})