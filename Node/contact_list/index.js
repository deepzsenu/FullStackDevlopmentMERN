const express = require("express");
const path = require("path");

const port = 8080;
const db = require("./config/mongoose.js");

const Contact = require("./models/contact.js");

const app = express();
Contact
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));


//app.use(express.urlencoded()) is a middle ware in this case
/* A middleware is a function which has access to our request and response
 - it can pre process the data and analyze our data before it reaches to another page or part 
 -  it has the capability to pass the data
 - some common things are done by the middle ware like converting data into key-value pairs 
    etc.

 */

app.use(express.urlencoded())

app.use(express.static('assets'));

// Middleware 1

app.use((req, res, next) => {
    // console.log("middleware1 is called! ");
    req.myName= "Deepak Kumar Saxena";
    next(); //this link wil allow middleware to run next code i
    // if we will not use the above next() function further code will not run

})

// middlewar2 

// app.use((req,res, next) => {
//     console.log("My Name from MW1", req.myName);
//     next();
// })

var contactList = [
    {
        name: "Deepak",
        phone: "111111111",
    },
    {
        name: "Tony",
        phone: "12434532432",
    },
    {
        name: "Stark",
        phone: "98793493",
    },
];

app.get("/", (req, res) => {
    // console.log(__dirname);
    // res.send("<h1>Cool it is running.<h1>");
    // console.log(req);
    // console.log("From the get route controller",req.myName);

    Contact.find({}).then( contact=> {

        // console.log('Found contacts:', contact);
        return res.render("home", {
            title: "contact list",
            contact_list: contact,
        });
      })
      .catch(error => {
        console.error('Error finding contacts:', error);
        return;
      });

    // return res.render("home", {
    //     title: "contact list",
    //     contact_list: contactList,
    // });
});

app.get("/contacts", (req, res) => {
    return res.render("contacts", { title: "contact list" });
    
});

//create contacts is a post request which is accepting the inputs from the form page.

app.post("/create_contact", (req, res)=>{
    // return res.redirect("/contacts");
    // console.log(req)
    // console.log(req.body);
    // console.log(req.body.name);
    // console.log(req.body.phone);

    // contactList.push({
    //     name: req.body.name,
    //     phone: req.body.phone,
    // })
    // contactList.push(req.body)//adding contact to the above array

    // using database for creating contacts
    // Contact.create({
    //     name: req.body.name,
    //     phone: req.body.phone,
    // }, (err, newContact)=>{
    //     if (err) {
    //         console.log("Error in creating a contact",err);
    //         return;
    //     }
    //     console.log("******",newContact);
    //     return res.redirect("back");

    // })
    const newContactData = {
        name: req.body.name,
        phone: req.body.phone,
    }

    Contact.create(newContactData).then(createdContact => {
        console.log('Contact created: Succesfully ');
        return res.redirect("back");
      })
      .catch(error => {
        console.error('Error creating contact:', error);
        return;
      });

    // return res.redirect("/"); // redirecting to our home page
})

// delete contact

app.get("/delete_contact", (req, res)=>{

    // deleting using mongodb
    // get the id from query parameters
    let id = req.query.id;

    // find the contact in the database using id and delete it.
    Contact.findByIdAndDelete(id).then(contact=> {
        console.log("Deleted Successfully");
        return res.redirect("back");
    }).catch(error=> {
        console.error("Error in deleting the contact", error);
        return;
    })



    // deleting using basic array 
    // console.log("Params are " , req.params);
    // console.log(req.query);
    // let phone =  req.query.phone; 
    // // console.log(phone);
    // let contactIndex = contactList.findIndex(contact => contact.phone == phone);

    // if (contactIndex > -1) {
    //     contactList.splice(contactIndex,1);
    // }

    // return res.redirect("/"); 

})



app.listen(port, function (err) {
    if (err) {
        console.log("you got an Error\n", err);
    }
    console.log("Server ready at Port:", port);
});
