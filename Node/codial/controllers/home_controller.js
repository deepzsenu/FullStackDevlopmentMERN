module.exports.home = (req, res)=>{
    // return res.end('<h1>Express is up!<h1>');

    return res.render('home',
    {
        title:"Home"
    });
}