const mongoose = require("mongoose");


mongoose.connect("mongodb://localhost/admin");

const db = mongoose.connection;

db.on('error', err => {
    console.log(err);
  });

db.once("open" , function(){
    console.log("Database is up and running!");
})