const mongoose = require("mongoose");


mongoose.connect("mongodb://localhost:27017/contact_list_db");

const db = mongoose.connection;

db.on('error', err => {
    console.log(err);
});

db.once("open" , function(){
    console.log("Database is up and running!");
})